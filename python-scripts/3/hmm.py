import numpy as np
import numpy as np, numpy.random
import matplotlib.pyplot as plt

from hmmlearn import hmm

# learn from dataZ --

startprob = np.random.dirichlet(np.ones(4),size=1) #np.array([0.6, 0.3, 0.1, 0.0])

# transition learn from dataZ

'''
transmat = np.array([[0.7, 0.2, 0.0, 0.1],
                     [0.3, 0.5, 0.2, 0.0],
                     [0.0, 0.3, 0.5, 0.2],
                     [0.2, 0.0, 0.2, 0.6]])
'''

a = np.random.dirichlet(np.ones(4),size=1)
b = np.random.dirichlet(np.ones(4),size=1)
c = np.random.dirichlet(np.ones(4),size=1)
d = np.random.dirichlet(np.ones(4),size=1)

transmat = np.array([a, b, c, d]) 

means = np.array([[1.0,  0.0],
                  [5.0, 6.0],
                  [3.0, 4.0],
                  [2.0, 1.0]])

covars = .9 * np.tile(np.identity(2), (4, 1, 1))

model = hmm.GaussianHMM(n_components=4, n_iter=100, init_params="mcs") #, covariance_type="full")

model.startprob_ = startprob
model.transmat_ = transmat
model.means_ = means
model.covars_ = covars

X, Z = model.sample(4)

print (Z)
