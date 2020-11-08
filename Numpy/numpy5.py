import numpy as np
a = np.random.randn((2, 4))
print(a)

# axis=0 column
# axis=1 row
print(np.sum(a, axis=1))
print(np.min(a, axis=0))
print(np.max(a, axis=1))
