import numpy as np
Y = np.array([[12,15,10,16,12],[5,9,14,7,10],[8,12,10,9,15]])
K = np.array([28,18,38])
doanhthu = np.dot(K,Y)
print(doanhthu)