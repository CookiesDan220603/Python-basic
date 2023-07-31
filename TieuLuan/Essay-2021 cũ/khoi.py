from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     

def req1(f, g, a):  ## KHONG XOA
	list1 =[None,None, None, None]
	try:
		list1[0] = round((diff(f+g,x,1)).subs(x,a),2)
	except:
		list1[0]= None
	try:
		list1[1] = round((diff(f*g,x,1)).subs(x,a),2)
	except:
		list1[1] = None
	try:
		list1[2] = round((diff(f.subs(x,g),x,1)).subs(x,a),2)
	except:
		list1[2] = None
	try:
		list1[3] = round((diff((f/g),x,1)).subs(x,a),2)
	except:
		list1[3]=None
	for i in range (0,4):
		if list1[i]== nan or list1[i]==zoo or list1[i]==-0.5*I:
			list1[i]=None
	return tuple(list1)

def sub(f,a,b,c):
	fx=f.subs(x,a)
	fy=fx.subs(y,b)
	fz=fy.subs(z,c)
	return fz
def req2(f, a, b, c):  ## KHONG XOA
	try:
		fall=sub(f,a,b,c)
		dfx= sub(diff(f,x),a,b,c)
		dfy= sub(diff(f,y),a,b,c)
		dfz= sub(diff(f,z),a,b,c)
		kq=dfx*(x-a)+dfy*(y-b)+dfz*(z-c)+fall
	except:
		kq = None
	if kq == nan or kq == zoo:
		kq = None	
	return kq

def req3(w, f1, f2, f3, a):  ## KHONG XOA
	try:
		w1=w.subs(x,f1)
		w2=w1.subs(y,f2)
		w3=w2.subs(z,f3)
		w4=diff(w3,t,1)
		kq=w4.subs(t,a)
	except:
		kq = None
	if kq == nan or kq == zoo:
		kq = None
	return kq  

def req8(f, eta, xi, tol): ## KHONG XOA
	try:
		df = diff(f,x)
		k=[]
		k.append(xi)
		for it in range(100):
			tam = k[-1]
			c = round(df.subs(x,tam),20)
			x_new = k[-1]-eta*c
			c= round(df.subs(x,x_new),20)
			if abs(c) < tol:
				break
			k.append(x_new)
		kq=k[-1]
		if kq == nan or kq == zoo:
			kq = None
		kq = float(round(kq,2))
		kq = round(kq,2)
		return kq
	except:
		kq = None


print(req1(1/x, x, 0))
print(req2(x**2 + y*z - 2*z**2, 1, 0, 1))
print(req3(0, cos(t), sin(t), t, 0))
print(req8(x**2 + 2*sin(x), 0.1, -5, 1e-3))
print(req8(x**2 + 2*x - 1, 0.1, -5, 1e-3))