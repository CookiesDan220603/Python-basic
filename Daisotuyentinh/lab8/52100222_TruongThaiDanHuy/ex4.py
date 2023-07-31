import numpy as np
import matplotlib.pyplot as plt
#Ex4
A = np.array([[1,2000],
              [1,6000],
              [1,20000],
              [1,30000],
              [1,40000]])
b = np.array([20,18,10,6,2])
w = np.linalg.inv(A.T@A)@A.T@b.T
print(w)
print("------------------------")

square_feet = 1000
y_price = w[0]*square_feet + w[1]

y_pred = w[0]*A[:,0] + w[1]
print(y_price)
fig = plt.figure()
plt.plot(A[:,0],b,'ro')

plt.show()