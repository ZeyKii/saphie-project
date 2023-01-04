from pydub import AudioSegment

main_audio = input("Main audio file path : ")
hidden_img = input("Hidden image file path : ")

sound1 = AudioSegment.from_file(main_audio)
sound1_1 = sound1.apply_gain(0)
sound2 = AudioSegment.from_file(hidden_img)
sound2_1 = sound2.apply_gain(+5)
combined = sound1_1.overlay(sound2_1)
destination = input("File path, name: ")
combined.export(destination + '.wav', format='wav')