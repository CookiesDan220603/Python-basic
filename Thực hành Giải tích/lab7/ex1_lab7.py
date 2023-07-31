import sympy as sp
x, y, z = sp.symbols("x, y, z")
def cau_a(f,a,b):
	value = f.subs({x:a,y:b})
	print("F[",a,",",b,"] = ",value)
def cau_b(f,a,b,c):
	value = f.subs({x:a,y:b,z:c})

	print("F[",a,",",b,",",c,"] = ",round(value,1))
#a
f= x**2 + x*(y**3)
print("ex1_a")
a=0
b=0
cau_a(f,a,b)
a=-1
b=1
cau_a(f,a,b)
a=2
b=3
cau_a(f,a,b)
a=-3
b=-2
cau_a(f,a,b)
#b
f = (x-y)/(y**2 + z**2)
print("ex1_b:")
a=3
b=-1
c =2
cau_b(f,a,b,c)
a=1
b=1/2
c=1/4
cau_b(f,a,b,c)
a=0
b=-1/3
c=0
cau_b(f,a,b,c)
a=2
b=2
c=100
cau_b(f,a,b,c)

