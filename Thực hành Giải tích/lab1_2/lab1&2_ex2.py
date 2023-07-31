import math
import numpy as np
def ex2a(x):
	res = 2 + (x**2)/((x**2)+4)
	return res
amin = math.inf
amax = -math.inf
for x in np.arange(-2,2.1,0.1):
	if ex2a(x) < amin :
		amin = ex2a(x)
	if ex2a(x)>amax :
		amax = ex2a(x)
print("The range of EX2_a is from " , round(amin,4), " to ", round(amax,4))

def ex2b(x):
	res = math.sqrt((5*x)+10)
	return res
bmin=math.inf
bmax=-math.inf
for x in np.arange(0,5.1,0.1):
	if ex2b(x) < bmin:
		bmin = ex2b(x)
	if ex2b(x) > bmax:
		bmax =ex2b(x)
print("The range of EX2_b is from " , round(bmin,4), " to ", round(bmax,4))
def ex2c(x):
	res= 2/((x*x)-16)
	return res
cmin = math.inf
cmax = -math.inf
for x in np.arange(5,10.1,0.1):
	if ex2c(x)<cmin:
		cmin = ex2c(x)
	if ex2c(x)>cmax:
		cmax = ex2c(x)
print("The range of EX2_c is from " , round(cmin,4), " to ", round(cmax,4))
dmin = math.inf
dmax = -math.inf
def ex2d(x):
	res = x**4 + 3*(x**2)-1
	return res
for x in np.arange(-3,3.1,0.1):
	if ex2d(x)<dmin:
		dmin = ex2d(x)
	if ex2d(x)>dmax:
		dmax = ex2d(x)
print("The range of EX2_d is from " , round(dmin,4), " to ", round(dmax,4))
def ex2e(x):
	if x >=0:
		return x
	else :
		return -x
emax=ex2e(3)
emin=ex2e(-3)
if emax < emin:
	emax=ex2e(-3)
	emin=ex2e(3)
print("The range of EX2_e is from " , round(emin,4), " to ", round(emax,4))
def ex2f(x):
	if x<0:
		return -x
	elif 0<=x and x<=1:
		return x**2
	else:
		return 1
a= ex2f(3)
b= ex2f(-3)
c= ex2f(1/2)
fmin= min(a,b,c)
fmax= max(a,b,c)
print("The range of EX2_f is from " , round(fmin,4), " to ", round(fmax,4))

