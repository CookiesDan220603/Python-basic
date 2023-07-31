import numpy as np
from matplotlib import pyplot as plt
def solve(A,b):
    return np.linalg.solve(A.T@A,A.T@b)
A=np.array([[1,2.1],
            [2,3.5],
            [3,4.2],
            [4,3.1],
            [5,4.4],
            [6,6.8]
])
b=np.array([[2.1],[3.5],[4.2],[3.1],[4.4],[6.8]])
print(solve(A,b))

data =[ [1,2.1],
        [2,3.5],
        [3,4.2],
        [4,3.1],
        [5,4.4],
        [6,6.8]
]
x,y=zip(*data)
plt.scatter(x,y)
plt.show()