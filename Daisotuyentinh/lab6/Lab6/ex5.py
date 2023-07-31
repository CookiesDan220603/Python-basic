import numpy as np

a = np.array([2, 3]).T
b = np.array([1, 2, 3]).T
c = np.array([1/2, -1/2, 1/4]).T
d = np.array([np.sqrt(2), 2, -(np.sqrt(2)), np.sqrt(2)]).T

uv = a / np.linalg.norm(a)
print(uv)

uv = b / np.linalg.norm(b)
print(uv)

uv = c / np.linalg.norm(c)
print(uv)

uv = d / np.linalg.norm(d)
print(uv)