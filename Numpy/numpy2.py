import numpy as np

a = np.array([2, 23, 4], dtype=np.int)
print(a)
print(a.dtype)

# 3 row 4 col, num = 0
b = np.zeros((3, 4))
print(b)


# 3 row 4 col, num = 1
c = np.ones((3, 4), dtype=np.int)
print(c)


d = np.ones((3, 4))
print(d)
print('-' * 20)

# !!! QUESTION !!! only comment code before, empty can output correct
ee = np.empty((3, 4))
print(ee)
