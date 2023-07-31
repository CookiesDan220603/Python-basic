import numpy as np
from sympy import *
A=np.array([[0.25,0.15,0.1],[0.4,0.15,0.2],[0.15,0.2,0.2]])
d=np.array([[100],[100],[100]])
I=np.array([[1,0,0],[0,1,0],[0,0,1]])
p=np.linalg.inv(I-A)@d
print("p={}".format(p))