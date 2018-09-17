import numpy as np

a = np.arange(12).reshape(4,3)
asum1 = a.sum(axis=0)
asum2 = a.sum(axis=1)

print (asum1, asum2)
