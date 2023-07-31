import numpy as np
A=np.array([[3,3.2],[3.5,3.6]])
B=np.array([[118.4],[135.2]])
root=np.linalg.solve(A,B)
children = round(float(root[0]))
adults = round(float(root[1]))
print("Number of children: {}".format(children))
print("Number of adults: {}".format(adults))