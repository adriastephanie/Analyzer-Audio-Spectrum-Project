#stream audio

import pyaudio
import numpy as np
from scipy.io.wavfile import write 
import util
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2048
RECORD_SECONDS = 10
 
audio = pyaudio.PyAudio()
 
# inicio da gravação 
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

print ("gravando................")
frames = np.array([])
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    
    frames = np.append(frames, data)

print ("finalizado a gravação - criado arquivo outputadria.wav")
  
write("outputadria.wav", RATE, frames) 
# parar gravação
stream.stop_stream()
stream.close()
audio.terminate()
 
print("Concluido!")