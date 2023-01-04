from pydub import AudioSegment

sound1 = AudioSegment.from_file(r"C:\Users\maxfe\saphie-project\TEST-AUDIO\electro_jazz.wav")
sound2 = AudioSegment.from_file(r"C:\Users\maxfe\saphie-project\TEST-AUDIO\Outro INSTRU.wav")

combined = sound1.overlay(sound2)

combined.export(r"C:\Users\maxfe\saphie-project\TEST-AUDIO\combined.wav", format='wav')