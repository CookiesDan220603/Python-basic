import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x,y= sp.symbols ('x,y')

def graph(f):
	fa = sp.lambdify((x,y),f,"numpy")
	#tao diem
	xa,ya = np.meshgrid(np.arange(-1,1,0.2),np.arange(-1,1,0.2))
	za = fa(xa,ya)
	#ve hinh
	fig = plt.figure()
	ax = fig.add_subplot(111,projection ="3d")
	ax.plot_surface(xa,ya,za,cmap =plt.cm.ocean,alpha =0.5)
	plt.xlabel("x0")
	plt.xlabel("y0")
	plt.title(str(f))
	plt.show()
#cau a
f = (sp.cos(x))*(sp.cos(y))*(pow(sp.exp(x),(sp.sqrt(x**2 + y**2))/4))
graph(f)
#cau b
f = (x*(y**2))/(x**2 + y**2)
graph(f)
#cau c
f = (x*y*(x**2 + y**2))/(x**2 + y**2)
graph(f)
#cau d
f = y**2 - y**4 - x**2
graph (f)
