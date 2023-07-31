import numpy as np
## Exercise 4

def a():
    u = np.array([1, 1])
    v = np.array([0, 1])
    print(np.sum(u*v))
a()

def b():
    u = np.array([1, 0])
    v = np.array([0, 1])
    print(np.sum(u*v))
b()
def c():
    u = np.array([-2, 3])
    v = np.array([1/2, -1/2])
    print(np.sum(u*v))
c()
def calc(u, v):
    return sum(u*v) / (np.linalg.norm(u, 2)*np.linalg.norm(v, 2))