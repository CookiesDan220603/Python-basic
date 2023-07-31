from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     

def req1(f, g, a):  ## KHONG XOA
	list1 =[None,None, None, None]
	list1[0] = round((diff(f+g,x,1)).subs(x,a),2)
	list1[1] = round((diff(f*g,x,1)).subs(x,a),2)
	list1[2] = round((diff(f.subs(x,g),x,1)).subs(x,a),2)
	list1[3] = round((diff((f/g),x,1)).subs(x,a),2)
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
	fall=sub(f,a,b,c)
	dfx= sub(diff(f,x),a,b,c)
	dfy= sub(diff(f,y),a,b,c)
	dfz= sub(diff(f,z),a,b,c)
	kq=dfx*(x-a)+dfy*(y-b)+dfz*(z-c)+fall
	if kq == nan or kq == zoo:
		kq = None	
	return kq


def req3(w, f1, f2, f3, a):  ## KHONG XOA
	w1=w.subs(x,f1)
	w2=w1.subs(y,f2)
	w3=w2.subs(z,f3)
	w4=diff(w3,t,1)
	kq=w4.subs(t,a)
	if kq == nan or kq == zoo:
		kq = None
	return kq  


def req4(a, b, n):  ## KHONG XOA
	k =n
	sum =0
	for j in range (0,n+1):
		sum += ((factorial(n))/((factorial(n-j))*factorial(j)))*(pow(a,n-j))*(pow(b,j))
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
  return (minima,maxima,saddle)


def req6(message, x, y, z):  ## KHONG XOA
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
	return chuoi


def req7(xp, yp, xs):  ## KHONG XOA
	k = len(yp)
	xp = np.array(xp, dtype = int)
	yp = np.array(yp, dtype = int)
	vlue = (sum(xp)*sum(yp)-k*sum(xp*yp))/((sum(xp)**2)-k*sum(xp**2))
	b = (1/k)*(sum(yp)-vlue*sum(xp))
	kq = round(vlue*xs+b,2)
	return kq


def req8(f, eta, xi, tol): ## KHONG XOA
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

print(req1(sqrt(x), 0, -1))
print(req2(x**2 + y*z - 2*z**2, 1, 0, 1))
print(req3(x**2 + y**2, cos(t), sin(t), t, 0))
print(req4(-x, 1, 2))
print(req5(3*y**2 - 2*y**3 -3*x**2 + 6*x*y))
print(req6('jgnnm',1,1,2))
print(req7([-2, 1, 4], [0, 2, 5], 3 ))
print(req8(x**2 + 2*x - 1, 0.1, -5, 1e-3))
print(req8(x**2 + 2*sin(x), 0.1, -5, 1e-3))
    
    
  
         