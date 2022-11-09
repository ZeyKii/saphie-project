import wave

def wav_byte(file):
    t = wave.open(file,"r")
    gm_bytes = wave.Wave_read.readframes(t, 5)
    return(gm_bytes)

print(wav_byte(r"C:\Users\alanw\saphie-project\Fonctions\test_audio.wav"))