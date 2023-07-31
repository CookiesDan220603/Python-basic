import numpy as np 
import math
import matplotlib.pyplot as plt

f_x = lambda x: math.sin(10 * math.pi / x)
x = np.arange(0.1, 4, 0.1)
y = list(map(f_x, x))

x_0 = [2, 1.5, 1.4, 1.3, 1.2, 1.1, 0.5, 0.6, 0.7, 0.8, 0.9]
a = 1
for x_2 in x_0:
	y_2 = math.sin(10*math.pi / x_2)
	slope = (y_2 - 0) / (x_2 - 1)
	plt.plot(x_2, y_2, 'yo')
	plt.plot([1, x_2], [0, y_2], color = 'red',label = 'PQ_' + str(a))
	a += 1
	plt.plot(x, y, color = 'cyan')
	plt.plot(1, 0, 'ro')
	plt.title("Slope = " + str(slope), fontsize = '13', color = 'green')
	plt.legend()
	plt.show()


