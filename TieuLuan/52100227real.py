from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     

def req1(f, g, a):  ## KHONG XOA
	solve = [ None, None, None, None]
	solve[0] = round(diff(f + g, x).subs(x, a),2)
	solve[1] = round(diff(f * g, x).subs(x, a),2)
	solve[2] = round(diff(f.subs(x, g),x).subs(x, a),2)
	if g==0 : 
		solve[3] = None 
	else : 
		solve[3] = round(diff(f/g, x).subs(x, a),2)
	return tuple(solve)
def xd(f,a,b,c):
  f1=f.subs(x,a)
  f2=f1.subs(y,b)
  f=f2.subs(z,c)
  return f
def req2(f, a, b, c):  ## KHONG XOA
	fabc=xd(f,a,b,c)
	solve_1= xd(diff(f,x),a,b,c)
	solve_2= xd(diff(f,y),a,b,c)
	solve_3= xd(diff(f,z),a,b,c)
	pttt=solve_1*(x-a)+solve_2*(y-b)+solve_3*(z-c)+fabc
	return pttt

def req3(w, f1, f2, f3, a):  ## KHONG XOA
	w = w.subs(x,f1)
	w = w.subs(y,f2)
	w = w.subs(z,f3)
	result = diff(w,t).subs(t,a)
	return result

def req4(a, b, n):  ## KHONG XOA
	result = 0
	for i in range ( 0, n + 1): 
		result += ((factorial(n)/(factorial(i) * factorial(n-i))) * (a**(n - i)*b**(i))) 
	return result


def req6(message, x, y, z):  ## KHONG XOA
	fx = abs(x**2 - y**2 - z)
	str = ""
	n = len(message)
	for i in range(0, n, 1):
		uni = ord(message[i]) #tra ve he thap phan trong bang ma ASCI2 
		kitu = np.bitwise_xor(fx, uni) #Cong nhi phan roi chuyen sang dang ki tu 
		str += chr(kitu) 
	return str

def req7(xp, yp, xc):  ## KHONG XOA
	n=len(xp)
	xp=np.array(xp)
	yp=np.array(yp)
	m=(sum(xp)*sum(yp)-n*sum(xp*yp))/(sum(xp)**2-n*sum(xp**2))
	b=(sum(yp)-m*sum(xp))/n
	ptxc=m*xc+b
	kq=round(ptxc,2)
	return kq 
def daoham(f,n):
   f2 = diff(f,x,1)
   f3 = lambdify(x,f2)(n)
   return f3
def req8(f, eta, xi, tol): ## KHONG XOA
	x_new = xi
	for i in range(10000):
		x_new -= eta*daoham(f,xi)
		if abs(daoham(f,x_new)) < tol:
			break
		xi = x_new
	f1 = round(x_new,2)
	return f1
print(req1(x**2 + 2*x,x**3, 1))
print(req2(x**2 + y**2 - 2*z**2 + z*log(z), 1, 1, 1))
print(req3(x*y + z, cos(t), sin(t), t, 0))
print(req4(2*x, -3, 4))
print(req6('khi*nol',1,3,2))
print(req7([-2, 0, 2], [0, 2, 3], 4 ))
print(req8(x**2 + 2*x - 1, 0.1, -5, 1e-3))


    
    
