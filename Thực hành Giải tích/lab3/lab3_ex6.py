import sympy as sp 
import numpy as np 

x = sp.symbols('x')
#Ex6_a
fx_6a = (x**2 - x -6)/(x-3)
# x=0
lim_fx6a_when_x_0 = sp.limit(fx_6a,x,0)
if (lim_fx6a_when_x_0==5):
	print ("Ex6a: The function is continuous at 0")
else :
	print("Ex6a: The function isn't continuous at 0")
# các điểm còn lại
for x_0 in np.arange(-100,100,1):
	if(x_0 != 0):
		limfx6a = sp.limit(fx_6a,x,x_0)
		if 	(limfx6a != fx_6a.subs(x,x_0)):
			print("Ex6a: The function isn't continuous at ", x_0)
			
print("Ex6a: The function is continuous at all x # 0 and x # 3")
print("")

#Ex6_b
fx_6b = (x**3 - 8) / (x*x - 4)

# x = 2
lim_fx6b_when_x_2 = sp.limit(fx_6b, x, 2)
if (lim_fx6b_when_x_2 == 3):
	print("Ex6b: The function is continuous at 2")
else:
	print("Ex6b: The function isn't continuous at 2")

lim_fx6b_when_x_negative_2 = sp.limit(fx_6b, x, -2)
if (lim_fx6b_when_x_negative_2 == 4):
	print("Ex6b: The function is continuous at -2")
else:
	print("Ex6b: The function isn't continuous at -2")

# Các điểm còn lại
for x_0 in np.arange(-100, 100, 1):
	if (x_0 != 2 and x_0 != -2):
		limfx6b = sp.limit(fx_6b, x, x_0)
		if (limfx6b != fx_6b.subs(x, x_0)):
			print("Ex6b: The function isn't continuous at ", x_0)

print("Ex6b: The function is continuous at all x # -2")
print("")

#Ex6_c
fx_6c = (x*x - x - 2) / (x - 2)

# x = 2
lim_fx6c_when_x_2 = sp.limit(fx_6c, x, 2)
if (lim_fx6c_when_x_2 == 1):
	print("Ex6c: The function is continuous at 2")
else:
	print("Ex6c: The function isn't continuous at 2")

# Các điểm còn lại
for x_0 in np.arange(-100, 100, 1):
	if (x_0 != 2):
		limfx6c = sp.limit(fx_6c, x, x_0)
		if (limfx6c != fx_6c.subs(x, x_0)):
			print("Ex6c: The function isn't continuous at ", x_0)
print("Ex6c: The function is continuous at all x # 2")
print("")

#Ex6_d
fx_6d = 1 / x*x 

# x = 0
lim_fx6d_when_x_0 = sp.limit(fx_6d, x, 0)
if (lim_fx6d_when_x_0 == 1):
	print("Ex6d: The function is continuous at 0")
else:
	print("Ex6d: The function isn't continuous at 0")

# Các điểm còn lại
for x_0 in np.arange(-100, 100, 1):
	if (x_0 != 0):
		limfx6d = sp.limit(fx_6d, x, x_0)
		if (limfx6d != fx_6d.subs(x, x_0)):
			print("Ex6d: The function isn't continuous at ", x_0)
print("Ex6d: The function is continuous at all x")
