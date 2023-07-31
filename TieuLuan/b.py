from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     
def req7(xp, yp, xs):  ## KHONG XOA
	k = len(yp)
	xp = np.array(xp, dtype = int)
	yp = np.array(yp, dtype = int)
	vlue = (sum(xp)*sum(yp)-k*sum(xp*yp))/((sum(xp)**2)-k*sum(xp**2))
	b = (1/k)*(sum(yp)-vlue*sum(xp))
	kq = round(vlue*xs+b,2)
	return kq
a = [-2,0,2]
c = [0,2,3]
d =4
print(req7(a,c,d))