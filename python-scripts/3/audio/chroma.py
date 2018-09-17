import vamp
import librosa

data, rate = librosa.load("example.wav")
chroma = vamp.collect(data, rate, "nnls-chroma:nnls-chroma")
stepsize, chromadata = chroma["matrix"]

import matplotlib.pyplot as plt

plt.imshow(chromadata)
plt.show()
