import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#a)
a1=2
a2=4
b1=3
b2=6
c1=6
c2=12
d1=200
d2=150
a3=6
b3=9
c3=18
d3=60
x,y=np.meshgrid(np.arange(-5,5),np.arange(-5,5))
z1=(d1-a1*x-b1*y)/c1
z2=(d2-a2*x-b2*y)/c2
z3=(d3-a3*x-b3*y)/c3
fig=plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.plot_surface(x,y,z1,cmap = plt.cm.ocean,alpha=0.5)
ax.plot_surface(x,y,z2,cmap = plt.cm.hsv,alpha=0.5)
ax.plot_surface(x,y,z3,cmap = plt.cm.rainbow,alpha=0.5)
plt.show()

