
import wave

def audio_message(file, message):
    song = wave.open(file, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    string = message
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)

    with wave.open('Nouvo son.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()

print(audio_message(r'C:\Users\alanw\saphie-project\Fonctions\Audio\Outro INSTRU.wav', "OUAIS"))

def decode_message(file):
    song = wave.open(file, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")[0]
    print("Sucessfully decoded: "+decoded)
    song.close()

print(decode_message(r'C:\Users\alanw\saphie-project\Nouvo son.wav'))