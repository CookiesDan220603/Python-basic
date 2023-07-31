import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x=sp.symbols('x')
dx = sp.symbols('dx')
fx= x**3 -3*x +1
#ex_a x=3
df_a= sp.diff(fx,x)
slope_a=  sp.limit(((fx.subs(x, 3 + dx) - fx.subs(x, 3)) / dx),dx,0)
val = np.arange(-2,10,0.1)
y_tagent = slope_a*(x-3)+ fx.subs(x,3)
f_val_a = sp.lambdify(x,fx,"numpy")(val)
f_tagent_a = sp.lambdify(x,y_tagent,"numpy")(val)
plt.plot(val,f_val_a,color='red',label='Fx_a')
plt.plot(val,f_tagent_a,color='blue',label='tagent_a')
plt.plot(3,fx.subs(x,3),'go',label='Point')
plt.grid(linestyle='--')
plt.legend()
plt.show()

#ex_b y= 9*x +2
y= 9*x +2
dt = sp.diff(fx-y)
solve = sp.solve(dt)
x1=solve[0]
x2=solve[1]
#x1

slope_b= sp.limit(((fx.subs(x, x1 + dx) - fx.subs(x, x1)) / dx),dx,0)
val = np.arange(-7,2,0.1)
y_tagent = slope_b*(x-x1)+ fx.subs(x,x1)
f_val_b = sp.lambdify(x,fx,"numpy")(val)
f_tagent_b = sp.lambdify(x,y_tagent,"numpy")(val)
plt.plot(val,f_val_b,color='red',label='Fx_b_x='+str(x1))
plt.plot(val,f_tagent_b,color='blue',label='tagent_a_x='+str(x1))
plt.plot(x1,fx.subs(x,x1),'go',label='Point')
plt.title("EX_b x="+str(x1))
plt.grid(linestyle='--')
plt.legend()
plt.show()

#x=2

slope_b= sp.limit(((fx.subs(x, x2 + dx) - fx.subs(x, x2)) / dx),dx,0)
val = np.arange(-2,10,0.1)
y_tagent = slope_b*(x-x2)+ fx.subs(x,x2)
f_val_b = sp.lambdify(x,fx,"numpy")(val)
f_tagent_b = sp.lambdify(x,y_tagent,"numpy")(val)
plt.plot(val,f_val_b,color='red',label='Fx_b_x='+str(x2))
plt.plot(val,f_tagent_b,color='blue',label='tagent_a_x='+str(x2))
plt.plot(x2,fx.subs(x,x2),'go',label='Point')
plt.title("EX_b x="+str(x2))
plt.grid(linestyle='--')
plt.legend()
plt.show()


#ex2_c A=[2/3,-1]
df_c= sp.diff(fx,x)
slope_c= df_a.subs(x,2/3)
val = np.arange(-5,5,0.1)
y_tagent = slope_c*(x-2/3)-1
f_val_c = sp.lambdify(x,fx,"numpy")(val)
f_tagent_c = sp.lambdify(x,y_tagent,"numpy")(val)
plt.plot(val,f_val_c,color='red',label='Fx_a')
plt.plot(val,f_tagent_c,color='blue',label='tagent_a')
plt.plot(2/3,-1,'go',label='Point')
plt.grid(linestyle='--')
plt.legend()
plt.show()






