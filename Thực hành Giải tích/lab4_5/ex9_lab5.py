import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x=sp.symbols('x')
fx= 4*(x**2) - x**3
df= sp.diff(fx,x)
#a [2,8]
slope_a= df.subs(x,2)
val = np.arange(0,4,0.1)
y_tagent = slope_a*(x-2)+ 8
f_val_a = sp.lambdify(x,fx,"numpy")(val)
f_tagent_a = sp.lambdify(x,y_tagent,"numpy")(val)
plt.plot(val,f_val_a,color='red',label='Fx_a')
plt.plot(val,f_tagent_a,color='blue',label='tagent_a')
plt.plot(2,8,'go',label='Point x=2')

# b[3,9]
slope_b= df.subs(x,3)
y_tagent = slope_a*(x-3)+ 9
f_tagent_b = sp.lambdify(x,y_tagent,"numpy")(val)
plt.plot(val,f_tagent_b,color='black',label='tagent_b')
plt.plot(3,9,'yo',label='Point x =3')
plt.title("Ex 9")
plt.legend()
plt.grid(linestyle='--')
plt.show()
