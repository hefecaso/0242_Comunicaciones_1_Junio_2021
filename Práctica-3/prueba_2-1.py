import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

wav = wave.open("output-audio.wav","rb")
raw = wav.readframes(-1)
raw = np.frombuffer(raw, "Int16")
sampleRate = wav.getframerate()

if wav.getnchannels()==2:
    print("Error, Use Mono Files")
    sys.exit(0)

Time = np.linspace(0, len(raw)/sampleRate, num = len(raw))

plt.title("Test")

plt.plot(Time, raw, color = "blue")

plt.ylabel("Amplitude")

plt.show()
