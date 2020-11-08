import numpy as np

A = np.arange(2,14).reshape((3,4))
print(A)
print('-' * 20)

# print(np.argmin(A))
# print(np.argmax(A))

# # Average
# print(A.mean())
# print(np.average(A))

# # Median
# print(np.median((A)))

# # Accumulate
# print(A)
# print(np.cumsum(A))
# print(np.diff(A))

# print(np.nonzero(A))
# print(np.sort(A))

# print(np.transpose(A))
# print(A.T)
# print((A.T).dot(A))

# print(np.clip(A, 5, 9))


print(np.mean(A, axis=0))
print(np.mean(A, axis=1))
