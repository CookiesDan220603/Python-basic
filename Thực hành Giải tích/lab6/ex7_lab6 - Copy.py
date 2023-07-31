#Exercise 7: Using a graph of the sequence to determine whether the sequence is convergent or divergent.
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math

n = symbols('n')

def graph(f, title):
	val = np.arange(1,250,1)
	fval = lambdify(n, f, "numpy")(val)
	plt.plot(val, fval, 'blue')
	plt.grid(linestyle = '--')
	plt.title(title, color = 'red')
	plt.plot(250, f.subs(n,250), 'ro')
	plt.show()

def mul(n):
	if n ==1: return 1
	return (2*n-1)*factorial(n-1)

#a
aa = 1 - (-2/exp(1))**n
title = "Cau a"
graph(aa, title)
print("---> Tu do thi, ta thay ham so hoi tu tai 1")

#b
ab = sqrt(n)*sin(pi/sqrt(n))
title = "Cau b"
graph(ab, title)
print("---> Tu do thi, ta thay ham so phan ky")

#c
ac = sqrt((3+2*n**2)/(8*n**2 + n))
title = "Cau c"
graph(ac, title)
print("---> Tu do thi, ta thay ham so hoi tu tai 0.5")

#d
ad = (n**2 * cos(n))/(1 + n**2)
title = "Cau d"
graph(ad, title)

#e
ae = mul(n)/factorial(n)
title = "Cau e"
f_val = []
val = np.arange(1,100,1)
for i in val:
  f_val.append(ae.subs(n,i))
plt.plot(val, f_val, "blue")
plt.title(title, color = 'red')
plt.show()

#f
af = mul(n)/(pow(2*n,n))
f_val = []
val = np.arange(1,100,1)
for i in val:
  f_val.append(ae.subs(n,i))
plt.plot(val, f_val, "blue")
plt.title("Cau f", color = 'red')
plt.show()
