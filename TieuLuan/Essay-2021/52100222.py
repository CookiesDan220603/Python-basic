from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     

def req1(f, g, a):  ## KHONG XOA
	list1 =[None,None, None, None]
	try:
		list1[0] = round((diff(f+g,x,1)).subs(x,a),2)
		if list1[0].is_real == False:
			list1[0]= None
	except:
		list1[0]= None
	try:
		list1[1] = round((diff(f*g,x,1)).subs(x,a),2)
		if list1[1].is_real == False:
			list1[1]= None
	except:
		list1[1] = None
	try:
		list1[2] = round((diff(f.subs(x,g),x,1)).subs(x,a),2)
		if list1[2].is_real == False:
			list1[2]= None
	except:
		list1[2] = None
	try:
		list1[3] = round((diff((f/g),x,1)).subs(x,a),2)
		if list1[3].is_real == False:
			list1[3]= None
	except:
		list1[3]=None
	if g==0:
		list1[3]=None
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
		if kq.is_real==False:
			kq = None
	except:
		kq = None	
	return kq


def req3(w, f1, f2, f3, a):  ## KHONG XOA
	try:
		w1=w.subs(x,f1)
		w2=w1.subs(y,f2)
		w3=w2.subs(z,f3)
		w4=diff(w3,t,1)
		kq=w4.subs(t,a)
		if kq.is_real==False:
			kq = None
	except:
		kq = None

	return kq

def req4(a, b, n):  ## KHONG XOA
	k =n
	sum =0
	try:
		for j in range (0,n+1):
			sum += ((factorial(n))/((factorial(n-j))*factorial(j)))*(pow(a,n-j))*(pow(b,j))
	except:
		sum = None
	return sum

def req5(f):  ## KHONG XOA
	dfx = diff(f,x,1)
	dfy = diff(f,y,1)
	rs= solve((dfx,dfy),dict = True)
	dfxx = diff(f,x,2)    
	dfyy = diff(f,y,2)               
	dfxy = diff(dfx,y,1) 
	minima = []
	maxima = []
	saddle = []
	try:
		for k in rs:
			if (k[x].is_real and k[y].is_real):
				check = lambdify((x,y), dfxx*dfyy - dfxy**2)(k[x],k[y])
				fxxcheck = lambdify((x,y), dfxx)(k[x],k[y])
				if (check>0) and (fxxcheck> 0):
					 minima.append((k[x],k[y]))
				if (check>0) and (fxxcheck < 0):
					maxima.append((k[x],k[y]))
				if (check<0):
					saddle.append((k[x],k[y]))
	except:
		minima = []
		maxima = []
		saddle = []

	return (minima,maxima,saddle)


def req6(message, x, y, z):  ## KHONG XOA
	try:
		fx = abs(x**2 - y**2 - z)
		ktu = bin(fx)
		k = len(message)
		array = []
		a =0
		while a < k: 
			array.append(ord(message[a]))
			a = a + 1
		array2 = []
		for b in array:
			array2.append(bin(b))
		array3 = []
		for c in array2:
			array3.append(int(ktu,2) ^ int(c,2)) 
		array4 = []
		for d in array3:
			array4.append(chr(d))
		chuoi = ""
		for e in array4:
			chuoi +=e
		if chuoi =="":
			chuoi ="None"
	except:
		chuoi ="None"
	return chuoi


def req7(xp, yp, xc):  ## KHONG XOA
	k = len(yp)
	xp = np.array(xp, dtype = int)
	yp = np.array(yp, dtype = int)
	vlue = (sum(xp)*sum(yp)-k*sum(xp*yp))/((sum(xp)**2)-k*sum(xp**2))
	b = (1/k)*(sum(yp)-vlue*sum(xp))
	kq = round(vlue*xc+b,2)
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
	except:
		return None
	kq=k[-1]
	kq = float(round(kq,2))
	kq = round(kq,2)
	if isinstance(kq,float) ==False:
		kq = None
	return kq
