from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     
#1
def req1(f, g, a):  ## KHONG XOA
	list1 =[]
	answer = round((diff(f+g,x,1)).subs(x,a),2)
	answer2 = round((diff(f*g,x,1)).subs(x,a),2)
	answer3 = round((diff(f.subs(x,g),x,1)).subs(x,a),2)
	answer4 = round((diff((f/g),x,1)).subs(x,a),2) 
	list1.append(answer)
	list1.append(answer2)
	list1.append(answer3)
	list1.append(answer4)
	return list1
# print(req1(x**2 + 2*x, x**3, 1))
print(req1(x**3, 2*x**5-7*x**2, 1))
#2
def xb(f,a,b,c):
  f1=f.subs(x,a)
  f2=f1.subs(y,b)
  f=f2.subs(z,c)
  return f
def req2(f,a,b,c):
  fabc=xb(f,a,b,c)
  df1= xb(diff(f,x),a,b,c)
  df2= xb(diff(f,y),a,b,c)
  df3= xb(diff(f,z),a,b,c)
  ytt=df1*(x-a)+df2*(y-b)+df3*(z-c)+fabc
  return ytt
f0=x**2 + y**2 - 2*z**2 + z*log(z)
a= 1
b= 1
c= 1
print(req2(x**2 + y*z - 2*z**2, 1, 0, 1))

#3
def req3(w, f1, f2, f3, a): ## KHONG XOA
	w1=w.subs(x,f1)
	w2=w1.subs(y,f2)
	w3=w2.subs(z,f3)
	w4=diff(w3,t,1)
	kq=w4.subs(t,a)
	return kq  
wa=x*y + z
f1a=cos(t)
f2a=sin(t)
f3a=t
a1= 0
print(req3(x**2 + y**2, cos(t), sin(t), t, 0))
#4
def req4(a, b, n):  ## KHONG XOA
	k =n
	sum =0
	for j in range (0,n+1):
		sum += ((factorial(n))/((factorial(n-j))*factorial(j)))*(pow(a,n-j))*(pow(b,j))
	return sum
print(req4(-x, 1, 2))

#6
def req6(message, x, y, z):  ## KHONG XOA
    f = abs(x**2 - y**2 - z)
    f1 = bin(f)
    f2 = len(message)
    f3 = []
    i =0
    while i < f2: 
      f3.append(ord(message[i]))
      i = i + 1
    f4 = []
    for n in f3:
      f4.append(bin(n))
    f5 = []
    for j in f4:
      f5.append(int(f1,2) ^ int(j,2)) 
    f6 = []
    for r in f5:
      f6.append(chr(r))
    f7 = ""
    for v in f6:
      f7 = f7 + v
    return f7
#7
a = [1,1,2]
b = 'jgnnm'
print(req6(b,1,1,2))
def req7(xp, yp, xs):  ## KHONG XOA
    n = len(yp)
    xp = np.array(xp, dtype = int)
    yp = np.array(yp, dtype = int)
    m = (sum(xp)*sum(yp)-n*sum(xp*yp))/((sum(xp)**2)-n*sum(xp**2))
    b = (1/n)*(sum(yp)-m*sum(xp))
    yc = m*xs+b
    yc = round(yc, 2)
    return yc
a = [-2,1,4]
c = [0,2,5]
d =3
print(req7(a,c,d))

#8
def req8(f, eta, xi, tol):
  df = diff(f,x)
  k=[]
  k.append(xi)
  for it in range(100):
    tam = k[-1]
    c = round(df.subs(x,tam),20)
    x_new = k[-1]-eta*c
    if abs(c) < tol:
      break
    k.append(x_new)
  kq = round(k[-1],2)
  return kq
x1 = req8(x**2 + 2*x - 1, 0.1, -5, 1e-3)
print(x1)