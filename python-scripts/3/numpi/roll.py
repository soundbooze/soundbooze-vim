import numpy as np

x = np.arange(10)
roll = np.roll(x, 2)

x2 = np.reshape(x, (2,5))
print (x2)

x2 = np.roll(x2, 1)
print (x2)

x2 = np.roll(x2, 1, axis=0)
print (x2)

x2 = np.roll(x2, 1, axis=1)
print (x2)
