import wave
import struct

def hide_image_in_audio(audio_filename, image_filename, output_filename):
  # Ouvrir le fichier audio en mode binaire en lecture
  with open(audio_filename, "rb") as audio_file:
    # Lire l'en-tête du fichier audio (44 octets)
    audio_header = audio_file.read(44)

    # Ouvrir le fichier image en mode binaire en lecture
    with open(image_filename, "rb") as image_file:
      # Lire les données binaires de l'image
      image_data = image_file.read()
      # Encoder les données binaires de l'image en tant que chaîne de caractères hexadécimaux
      image_hex_data = image_data.hex()

      # Lire les données binaires du fichier audio (après l'en-tête)
      audio_data = audio_file.read()

      # Remplacer les N premiers octets des données audio par les données binaires de l'image, où N est la longueur de l'image en octets
      N = len(image_data)
      hidden_audio_data = image_data + audio_data[N:]

      # Ouvrir le fichier audio de sortie en mode binaire en écriture
      with open(output_filename, "wb") as output_file:
        # Écrire l'en-tête du fichier audio
        output_file.write(audio_header)
        # Écrire les données audio modifiées avec l'image cachée
        output_file.write(hidden_audio_data)