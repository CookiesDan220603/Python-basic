import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
def graph(f,a,b,n):
	val = np.arange(a,b,0.1)
	f_val = sp.lambdify(x,f,'numpy')(val)
	plt.plot(val,f_val)
	delta_x = (b-a)/n
	xi =[a]
	yi = [f.subs(x,a).evalf()]
	area = 0.0
	for i in range(n): #chia thanh n hinh chu nhat
		xi.append(xi[-1]+delta_x) # Day la x(i+1)= xi + delta_x
		yi.append(f.subs(x,xi[-1]).evalf()) # f(x(i+1))
		area += yi[-1]*delta_x
	print("area = {}".format(area))
	for i in range(len(xi)):
		plt.plot([xi[i],xi[i]],[0,yi[i]])
	plt.show()

x = sp.symbols('x')
#Ex8a
f = (1-x)
print("Ex 8a ")
graph(f,0,1,4)
graph(f,0,1,100)
graph(f,0,1,200)
fin = sp.integrate(f,(x,0,1))
print("Average of fx = ",fin)
print("---------------------")

#Ex8b
f = sp.cos(x)
print("Ex 8b")
a = -np.pi
b = np.pi
graph(f,a,b,4)
graph(f,a,b,100)
graph(f,a,b,200)
fin = sp.integrate(f,(x,a,b))
print("Average of fx = ",fin)
print("--------------------")
#Ex8c
f = x**2 + 1
print("Ex 8c")
a = 0
b = 1
graph(f,a,b,4)
graph(f,a,b,100)
graph(f,a,b,200)
fin = sp.integrate(f,(x,a,b))
print("Average of fx = ",fin)
print("--------------------")
#Ex8d
f = abs(x)
print("Ex 8d")
a = -1
b = 1
graph(f,a,b,4)
graph(f,a,b,100)
graph(f,a,b,200)
fin = sp.integrate(f,(x,a,b))
print("Average of fx = ",fin)
print("--------------------")

