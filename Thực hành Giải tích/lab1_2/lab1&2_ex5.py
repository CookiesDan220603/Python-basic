import matplotlib.pyplot as plt
import numpy as np
from sympy import*
import math
x=symbols('x')
f = sqrt(abs(x))
val = np.arange(-4,4,0.1) #giá trị x
f_val = lambdify(x,f,"numpy")(val) #giá trị y tương ứng vs x
plt.plot(val,f_val,'r')
plt.plot('f(x) = sqrt(abs(x))')
plt.grid(linestyle = '-')
plt.show()
f = x**4 +3*(x**2)-1
val = np.arange(-4,4,0.1) #giá trị x
f_val = lambdify(x,f,"numpy")(val) #giá trị y tương ứng vs x
plt.plot(val,f_val,'r')
plt.plot('f(x) = x^4 +3*(x^2)-1')
plt.grid(linestyle = '-')
plt.show()
f = x**3 +x
val = np.arange(-4,4,0.1) #giá trị x
f_val = lambdify(x,f,"numpy")(val) #giá trị y tương ứng vs x
plt.plot(val,f_val,'r')
plt.plot('f(x) = x^3 +x')
plt.grid(linestyle = '-')
plt.show()
f =exp(x)
val = np.arange(-4,4,0.1) #giá trị x
f_val = lambdify(x,f,"numpy")(val) #giá trị y tương ứng vs x
plt.plot(val,f_val,'r')
plt.plot('f(x) = e^x')
plt.grid(linestyle = '-')
plt.show()
f = log(x)
val = np.arange(-4,4,0.1) #giá trị x
f_val = lambdify(x,f,"numpy")(val) #giá trị y tương ứng vs x
plt.plot(val,f_val,'r')
plt.plot('f(x) = ln(x)')
plt.grid(linestyle = '-')
plt.show()
f=(2*(x**2)-3)/(7*x+4)
val = np.arange(-4,4,0.1) #giá trị x
f_val = lambdify(x,f,"numpy")(val) #giá trị y tương ứng vs x
plt.plot(val,f_val,'r')
plt.plot('f(x) = 2*(x^2)-3)/(7*x+4)')
plt.grid(linestyle = '-')
plt.show()

