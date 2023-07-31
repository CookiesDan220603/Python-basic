import sympy as sp 
import numpy as np 

x = sp.symbols('x')

fx = 1 - pow(1 - x**2,1/2)
lim_1 = sp.limit(fx,x,1)
lim_negative_1 = sp.limit(fx,x,-1)
if(lim_1==lim_negative_1):
	print("Ham so lien tuc trong doan tu [-1;1]")
else :
	print("Ham so khong lien tuc trong doan tu [-1;1]")
'''continuous = True
for c in np.arange(-1,1.001,0.001):
	c= round(c,3)
	lm = sp.limit(fx,x,c)
	if lm != fx.subs(x,c):
		print("HAM SO KHONG LIEN TUC")
		continuous = False
if continuous == True:
	print ("Ham so lien tuc")
'''