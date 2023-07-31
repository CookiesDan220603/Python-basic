import numpy as np
from sympy import total_degree
icecream = np.array([[12,15,10,16,12],[5,9,14,7,10],[8,12,10,9,15]])
money = np.array([28,18,38])
total = np.dot(money,icecream)
print(total)