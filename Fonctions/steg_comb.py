from pydub import AudioSegment

sound1 = AudioSegment.from_file(r"C:\Users\alanw\saphie-project\Fonctions\Audio\Outro INSTRU.wav")
sound1_1 = sound1.apply_gain(0)
sound2 = AudioSegment.from_file(r"C:\Users\alanw\saphie-project\Fonctions\TEST.png.wav")
sound2_1 = sound2.apply_gain(+5)

combined = sound1_1.overlay(sound2_1)

combined.export(r"C:\Users\alanw\saphie-project\Fonctions\Audio\OUTRO_MODIF.wav", format='wav')