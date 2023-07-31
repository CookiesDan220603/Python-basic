import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([7, 4, 3])
v3 = np.array([2, 1, 9])

print(np.linalg.norm(v2 - v1))
print(np.linalg.norm(v3 - v2))
print(np.linalg.norm(v1 - v3))