import sympy as sp
x=sp.symbols('x')

def ex8 (f,a,b,e):
	d= b-a
	while b-a>=e :
		d=0.618*d
		x1=b-d
		x2=a+d
		if f.subs(x,x1) >f.subs(x,x2):
			b=x2
		else:
			a=x1
	print([a,b])	
#ex 8a
f = -2*x**2 + x + 4
a =-5
b = 5
e = 1/3
print("ex8 a")
ex8(f,a,b,e)
#ex 8b
f = -4*x**2 + 2*x + 2
a =-6
b = 6
e = 1/10
print("ex8 b")
ex8(f,a,b,e)
#ex 8c
f = x**3 + 6*x**2 + 5*x -12
a =-5
b = -2
e = 1/10
print("ex8 c")
ex8(f,a,b,e)
#ex 8d
f = 2*x - x**2
a =0
b = 3
e = 1/100
print("ex8 d")
ex8(f,a,b,e)
#ex 8e
f = x**2 - x -10
a =-10
b = 10
e = 1/5
print("ex8 e")
ex8(f,a,b,e)
