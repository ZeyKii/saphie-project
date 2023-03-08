import numpy as np
from PIL import Image
import codecs

def hide_text_in_image(image_path, text_to_hide, encoding):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    image = np.array(image)
    # Encode the text to hide into bytes using the specified encoding
    encoded_text = text_to_hide.encode(encoding)
    # Convert the encoded text to a binary string
    binary_text = ''.join(format(b, 'b') for b in encoded_text)
    # Add the text length to the beginning of the binary string
    binary_text = format(len(encoded_text), 'b').zfill(16) + binary_text
    # Iterate through the binary string, and hide each bit in the least significant bit of the image's pixels
    for i, bit in enumerate(binary_text):
        x, y = i // image.shape[1], i % image.shape[1]
        image[x, y] = (image[x, y] & ~1) | int(bit)
    # Save the modified image
    Image.fromarray(image).save("hidden.png")

def retrieve_text_from_image(image_path, encoding):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    image = np.array(image)
    # Get the length of the encoded text to be retrieved from the first 16 bits
    text_length = int(''.join([str(image[i // image.shape[1], i % image.shape[1]][0] & 1) for i in range(16)]), 2)
    # Retrieve the encoded text by getting the least significant bit of every pixel
    binary_text = ''.join([str(image[i // image.shape[1], i % image.shape[1]][0] & 1) for i in range(16, 16 + text_length * 8)])
    # Convert the binary string to bytes
    encoded_text = bytes(int(binary_text[i:i+8], 2) for i in range(0, len(binary_text), 8))
    # Decode the encoded text using the specified encoding
    text = encoded_text.decode(encoding)
    return text

# Example usage:
text_to_hide = "coucou"
encoding = "latin1"
hide_text_in_image(r"C:\Users\maxfe\saphie-project\Fonctions\Image\nightcity.jpeg", text_to_hide, encoding)
retrieved_text = retrieve_text_from_image(r"C:\Users\maxfe\saphie-project\Fonctions\hidden.png", encoding)
print(retrieved_text)
