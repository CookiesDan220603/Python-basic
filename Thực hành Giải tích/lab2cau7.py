import matplotlib.pyplot as plt 
import math
import numpy as np

#function_x
def Function_x(x):
	return 4 * pow(math.sin(x), 5) + 5

#function_y
def Function_y(x):
	return 3 * math.cos(x) - 1.7 * math.cos(2 * x) - math.cos(3 * x) + 1

x = np.arange(0, 2 * math.pi, 0.1, dtype = float)
y = list(map(Function_x, x))
z = list(map(Function_y, x))
plt.plot(x, y, label = 'Function_x', color = 'pink')
plt.plot(x, z, label = 'Function_y', color = 'cyan')
plt.title("The of of the function x & y")
plt.legend()
plt.grid(linestyle = '--')
plt.show()