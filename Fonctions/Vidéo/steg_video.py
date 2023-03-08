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

def extract_message_from_video(video_path):
    # Ouvrir la vidéo en mode lecture
    video_capture = cv2.VideoCapture(video_path)

    # Extraire le message caché dans chaque trame de la vidéo
    binary_message = ""
    frame_num = 0
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            # Extraire les bits du message des canaux de couleur de chaque pixel de la trame
            for i in range(frame.shape[0]):
                for j in range(frame.shape[1]):
                    for c in range(3):
                        pixel_value = frame[i, j, c]
                        binary_message += bin(pixel_value)[-1]

            frame_num += 1
        else:
            break

    # Convertir les bits extraits en octets pour récupérer le message original
    message = ""
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))

    # Fermer la capture vidéo
    video_capture.release()

    return message


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hide and extract message in video')
    parser.add_argument('--hide', action='store_true', help='Hide message in video')
    parser.add_argument('--extract', action='store_true', help='Extract message from video')
    parser.add_argument('--video_path', type=str, help='Path to video file')
    parser.add_argument('--message', type=str, help='Message to hide in video')
    args = parser.parse_args()

    if args.hide:
        hide_message_in_video(args.video_path, args.message)
    elif args.extract:
        message = extract_message_from_video(args.video_path)
        print(message)
    else:
        parser.print_help()