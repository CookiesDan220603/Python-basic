import numpy as np
import matplotlib.pyplot as plt
A=np.array([[1,1,1],[1,2,4],[1,3,9]])
B=np.array([[6],[15],[38]])
a=np.linalg.solve(A,B)
t=np.arange(-10,10)
yt = a[0]+a[1]*t+a[2]*t**2
t_s = 6.5
y_s = a[0]+a[1]*t_s+a[2]*(t_s)**2
fig=plt.figure()
plt.plot(t,yt)
plt.plot(t_s,y_s,'ro')
plt.show()
