import numpy as np

x = np.array([1, 2, 3])
y = np.array([98, 12, 33])
z = np.hstack((x, y))
print("x = ", x)
print("y =", y)
print("z =", z)