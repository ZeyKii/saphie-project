from PIL import Image

def encode(image, message):
  # Convertir l'image en objet pixel map
  pixel_map = image.load()

  # Récupérer la taille de l'image
  (width, height) = image.size

  # Convertir le message en binaire
  binary_message = bin(int.from_bytes(message.encode(), 'big'))[2:]

  # Ajouter des "0" jusqu'à ce que la longueur du message binaire soit un multiple de 3
  while len(binary_message) % 3 != 0:
    binary_message = "0" + binary_message

  # Cacher le message binaire dans l'image
  for i in range(0, len(binary_message), 3):
    # Récupérer les 3 bits du message
    bits = binary_message[i:i+3]

    # Récupérer l'index du pixel à modifier
    x = i // 3 % width
    y = i // 3 // width

    # Récupérer la valeur du pixel
    (r, g, b) = pixel_map[x, y]

    # Modifier les 3 bits de poids faible des composantes RGB
    pixel_map[x, y] = (r // 2 * 2 + int(bits[0]), g // 2 * 2 + int(bits[1]), b // 2 * 2 + int(bits[2]))

def decode(image):
  # Convertir l'image en objet pixel map
  pixel_map = image.load()

  # Récupérer la taille de l'image
  (width, height) = image.size

  # Récupérer le message binaire caché dans l'image
  binary_message = ""
  for y in range(height):
    for x in range(width):
      # Récupérer la valeur du pixel
      (r, g, b) = pixel_map[x, y]

      # Récupérer les 3 bits de poids faible des composantes RGB
      binary_message += str(r % 2)
      binary_message += str(g % 2)
      binary_message += str(b % 2)

  # Supprimer les "0" ajoutés lors de l'encodage
  binary_message = binary_message.rstrip("0")

  # Convertir le message binaire en chaîne de caractères
  message = int(binary_message, 2).to_bytes((len(binary_message) + 7) // 8, 'big').decode()

  return message

def main():
  # Ouvrir l'image
  image = Image.open(r"C:\Users\alanw\saphie-project\Fonctions\Image\TEST.png")

  # Encoder un message dans l'image
  encode(image, "Ceci est un message secret !")

  # Sauvegarder l'image modifiée
  image.save("image_modified.png")
main()