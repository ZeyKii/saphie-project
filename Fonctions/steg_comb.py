import wave

def superpose_audio(audio_file_1, audio_file_2, output_file):
    # Ouvrez les deux fichiers audio en mode lecture
    wave_1 = wave.open(audio_file_1, 'rb')
    wave_2 = wave.open(audio_file_2, 'rb')

    # Obtenez les paramètres audio (nombre de canaux, taux d'échantillonnage, etc.)
    audio_params = wave_1.getparams()

    # Ouvrez le fichier de sortie en mode écriture
    wave_out = wave.open(output_file, 'wb')

    # Définissez les paramètres audio du fichier de sortie
    wave_out.setparams(audio_params)

    # Créez une boucle infinie pour lire les deux fichiers audio
    while True:
        # Lisez un bloc de données audio du premier fichier
        audio_data_1 = wave_1.readframes(1024)

        # Si vous avez atteint la fin du premier fichier, commencez à lire à partir du début
        if not audio_data_1:
            wave_1.rewind()
            audio_data_1 = wave_1.readframes(1024)

        # Lisez un bloc de données audio du deuxième fichier
        audio_data_2 = wave_2.readframes(1024)

        # Si vous avez atteint la fin du deuxième fichier, commencez à lire à partir du début
        if not audio_data_2:
            wave_2.rewind()
            audio_data_2 = wave_2.readframes(1024)

        # Superposez les deux blocs de données audio
        audio_data_out = audio_data_1 + audio_data_2

        # Écrivez le bloc de données audio superposées dans le fichier de sortie
        wave_out.writeframes(audio_data_out)

    # Fermez les fichiers audio
    wave_1.close()
    wave_2.close()
    wave_out.close()

# Appelez la fonction pour superposer les fichiers audio "audio_file_1.wav" et "audio_file_2.wav"
# et enregistrer le résultat dans le fichier "output_file.wav"
