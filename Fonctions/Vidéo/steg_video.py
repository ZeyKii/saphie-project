import cv2
import argparse
import numpy as np

def hide_message_in_video(video_path, message):
    # Ouvrir la vidéo en mode écriture
    video_capture = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_writer = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

    # Convertir le message en binaire
    binary_message = ''.join(format(ord(i), '08b') for i in message)

    # Cacher le message dans chaque trame de la vidéo
    frame_num = 0
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            # Créer une copie de la trame originale
            modified_frame = frame.copy()

            # Cacher les bits du message dans les canaux de couleur de chaque pixel de la trame originale
            for i, bit in enumerate(binary_message):
                row = i // width
                col = i % width
                for c in range(3):
                    pixel_value = modified_frame[row, col, c]
                    new_pixel_value = int(bin(pixel_value)[2:-1] + bit, 2)
                    modified_frame[row, col, c] = new_pixel_value

            # Ajouter la trame modifiée à la vidéo de sortie
            video_writer.write(modified_frame)
            frame_num += 1
        else:
            break

    # Fermer les captures vidéo
    video_capture.release()
    video_writer.release()

def decode_hidden_message(video_path):
    # Ouvrir la vidéo en mode lecture
    video_capture = cv2.VideoCapture(video_path)

    # Extraire les informations sur la vidéo
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Initialiser le message binaire caché
    binary_message = ''

    # Lire chaque trame de la vidéo et extraire les bits cachés dans les canaux de couleur
    frame_num = 0
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            # Parcourir chaque pixel de la trame et extraire les bits cachés
            for row in range(height):
                for col in range(width):
                    # Parcourir les canaux de couleur
                    for c in range(3):
                        pixel_value = frame[row, col, c]
                        hidden_bits = bin(pixel_value)[-1]
                        binary_message += hidden_bits

            frame_num += 1
        else:
            break

    # Fermer la capture vidéo
    video_capture.release()

    # Convertir le message binaire en texte
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    return message

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hide or extract a message from a video')
    parser.add_argument('--hide', action='store_true', help='hide a message in the video')
    parser.add_argument('--extract', action='store_true', help='extract a hidden message from the video')
    parser.add_argument('--video', type=str, help='path to the input video')
    parser.add_argument('--message', type=str, help='the message to be hidden')
    args = parser.parse_args()
    if args.hide:
         hide_message_in_video(args.video, args.message)
    elif args.extract:
        message = decode_hidden_message(args.video)
        print(message)
    else:
        print("Please specify either --hide or --extract.")