import math
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x = symbols('x')
#Ex_4.1
f = sin(1/x)
lim = limit(f,x,0,'+')
print("4.1-The limit of fx when x tend to 0+ is: {}".format(lim))
print("   -The limit dose not exits ")
#Ex_4.2
f = sin(1/x)
lim = limit(f,x,0,'-')
print("4.2-The limit of fx when x tend to 0- is: {}".format(lim))
print("   -The limit dose not exits ")
#Ex_4.3
f = sin(1/x)
lim = limit(f,x,0)
print("4.3-The limit of fx when x tend to 0 is: {}".format(lim))
print("   -The limit dose not exits ")
def f4(x):
    if x <= 0:
        return 0
    else:
        return math.sin(1/x)
x1 = np.arange(-100,1,1)
y1 = list(map(f4, x1))

x2 = np.arange(0.01,100,0.01)
y2 = list(map(f4, x2))
plt.title("Lab 3 exercise 4 ")
plt.plot(x1,y1,'r')
plt.plot(x2,y2,'m')
plt.grid()
plt.show()
