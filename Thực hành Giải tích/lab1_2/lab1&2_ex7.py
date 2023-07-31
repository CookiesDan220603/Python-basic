import matplotlib.pyplot as plt
import numpy as np
from sympy import*
import math
t=np.arange(-10,10,0.01)
x = 4*np.sin(t)**5 + 5
y = 3 * np.cos(t) - 1.7 * np.cos(2 * t) - np.cos(3 * t) + 1
plt.plot(x,y,'r')
plt.grid(linestyle = '-')
plt.plot(x,y,'c')
plt.text(4.6,1,'LOVE',fontsize =15,color='red')
plt.show()
