from pydub import AudioSegment
import os, platform


system = platform.system()

if system == "Windows":
    os.system("cls")
else :
    os.system("clear")
print("The image was successfully converted!\n")
main_audio = input("Main audio file path : ")

if system == "Windows":
    os.system("cls")
else :
    os.system("clear")
    
print("It is in the same folder as the previously chosen image\n")
hidden_img = input("Hidden image file path : ")

if system == "Windows":
    os.system("cls")
else :
    os.system("clear")

sound1 = AudioSegment.from_file(main_audio)
sound1_1 = sound1.apply_gain(0)
sound2 = AudioSegment.from_file(hidden_img)
sound2_1 = sound2.apply_gain(+5)
combined = sound1_1.overlay(sound2_1)
destination = input("File path, name: ")
combined.export(destination + '.wav', format='wav')