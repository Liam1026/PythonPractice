# copy & deep copy
import numpy as np

a = np.arange(4)
b = a
c = a
d = b
a[0] =11
print(a)
print(b)
print(c)
print(d)

print(b is a)
d[1:3] = [22,33]
print(a,b,c,d)

b = a.copy()  # deep copy
a[3] = 44
print(b)
print(a)
