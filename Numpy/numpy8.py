# Merge
import numpy as np

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A,B)) # vertical stack
print(A.shape, C.shape)

D = np.hstack((A,B)) # horizontal stack
print(D)
print(D.shape)  # element

print(A.T.shape)

# newaxis = add dimension
print(A[:, np.newaxis]) # row -->coloum
print(A[:, np.newaxis].shape)

# multipe array merge 
E = np.concatenate((A,B,B,A), axis=0)
print(E)


