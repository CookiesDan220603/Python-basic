import matplotlib.pyplot as plt 
import numpy as np
import math 

#cau10_a
def Function10_a(x, k):
	return pow(x, 2) + k

x = np.arange(-10, 10.1, 0.1, dtype = float)
k = np.arange(2, 14, 2)

for ki in k:
	y = []
	for xi in x:
		y.append(Function10_a(xi, ki))
	plt.plot(x, y, label = 'k = ' + str(ki))

plt.title("Exercise 10_a")
plt.legend()
plt.show()

#cau10_b
def Function10_b(x, k):
	return pow((x + k), 2)

x = np.arange(-10, 10.1, 0.1, dtype = float)
k = np.arange(2, 14, 2)

for ki in k:
	y = []
	for xi in x:
		y.append(Function10_b(xi, ki))
	plt.plot(x, y, label = "k = " + str(ki))
plt.title("Exercise 10_b")
plt.legend()
plt.show()

#cau10_c
def Function10_c(x, k):
	return k * math.sqrt(x)

x = np.arange(1, 50.1, 0.1, dtype = float)
k = [1/3, 1, 3, 6]

for ki in k:
	y = []
	for xi in x:
		y.append(Function10_c(xi, ki))
	plt.plot(x, y, label = 'k = ' + str(ki))

plt.title("Exercise 10_c")
plt.legend()
plt.show()

#cau10_d
def Function10_d(x):
	return pow(x, 3)

x = np.arange(-10, 10, 0.1, dtype = float)
y = np.array(list(map(Function10_d, x)))
plt.plot(x, y, label = 'Original graph', color = 'cyan')
plt.plot(x - 1, y - 1, label = 'Shifted graph', color = 'pink')
plt.title("Exercise 10_d")
plt.legend()
plt.grid(linestyle = '--')
plt.show()

#cau10_e
def Function10_e(x):
	return pow(x, 2/3)

x = np.arange(0.1, 20, 0.1, dtype = float)
y = np.array(list(map(Function10_e, x)))
plt.plot(x, y, label = 'Original graph', color = 'magenta')
plt.plot(x + 1, y - 1, label = 'Shifted graph', color = 'green')
plt.title("Exercise 10_e")
plt.legend()
plt.grid(linestyle = '--')
plt.show()

#cau10_f
def Function10_f(x):
	return 1/2 * (x + 1) + 5 
x = np.arange(-10, 10, 0.1, dtype = float)
y = np.array(list(map(Function10_f, x)))
plt.plot(x, y, label = 'Original graph', color = 'magenta')
plt.plot(x + 1, y - 5, label = 'Shifted graph', color = 'orange')
plt.title("Exercise 10_f")
plt.legend()
plt.grid(linestyle = '--')
plt.show()

#cau10_g
def Function10_g(x):
	return 1 / pow(x, 2)

x = np.arange(-10, 10, 0.13, dtype = float)
y = np.array(list(map(Function10_g, x)))
plt.plot(x, y, label = 'Original graph', color = 'orange')
plt.plot(x - 2, y - 1, label = 'Shifted graph', color = 'green')
plt.title("Exercise 10_g")
plt.legend()
plt.grid(linestyle = '--')
plt.show()

#cau10_h
def Function10_h(x):
	return 1 - pow(x, 3)

x = np.arange(-10, 10, 0.1, dtype = float)
y = list(map(Function10_h, x))
y_stretched = list(map(Function10_h, x / 2))
plt.plot(x, y, label = 'Original graph', color = 'cyan')
plt.plot(x, y_stretched, label = 'Stretched horizontally graph')
plt.title("Exercise 10_h")
plt.legend()
plt.grid(linestyle = '--')
plt.show() 

#cau10_i	
def Function10_i(x):
	return math.sqrt(x + 1)
x = np.arange(0, 20, 0.1, dtype = float)
y = list(map(Function10_i, x))
y_compressed = list(map(Function10_i, 4 * x))
plt.plot(x, y, label = 'Original graph', color = 'pink')
plt.plot(x, y_compressed, label = 'Compressed horizontally graph')
plt.title("Exercise 10_i")
plt.legend()
plt.grid(linestyle = '--')
plt.show()

#cau10_j
def Function10_j(x):
	return math.sqrt(x + 1)
x = np.arange(0, 20, 0.1, dtype = float)
y = np.array(list(map(Function10_j, x)))
plt.plot(x, y, label = 'Original graph', color = 'magenta')
plt.plot(x, 3 * y, label = 'Stretched vertically graph')
plt.title("Exercise 10_j")
plt.legend()
plt.grid(linestyle = '--')
plt.show()