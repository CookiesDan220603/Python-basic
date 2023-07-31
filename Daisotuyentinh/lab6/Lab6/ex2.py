import numpy as np

B1 = np.array([[1, -7], [-2, -3]])
print( max( np.sum( abs( B1), axis=1)))
    
B2 = np.array([[3, 6], [1, 0]])
print( max( np.sum( abs( B2), axis=1)))

B3 = np.array([[5, -4, 2], [-1, 2, 3], [-2, 1, 0]])
print( max( np.sum( abs( B3), axis=1)))

B4 = np.array([[3, 6, -1], [3, 1, 0], [2, 4, -7]])
print( max( np.sum( abs( B4), axis=1)))

B5 = np.array([[3, 0, 0], [0, 4, 0], [0, 0, 2]])
print( max( np.sum( abs( B5), axis=1)))
