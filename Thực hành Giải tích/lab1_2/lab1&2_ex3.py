import sympy as sp
import math
def even_function(x,f):
	if f(x)==f(-x):
		return True
	else:
		return False
def odd_function(x,f):
	if f(x)==-f(-x):
		return True
	else :
		return False
#Ex3_a
x = sp.symbols('x')
f = lambda x: x**(-5)
if even_function(x,f)== True:
	print("a) This is a enven function")
elif odd_function(x,f)== True:
	print("a) This is a odd function")
else :
	print("a) This is not a even or odd function")
#Ex3_b
f = lambda x: x**2+x
if even_function(x,f)== True:
	print("b) This is a enven function")
elif odd_function(x,f)== True:
	print("b) This is a odd function")
else :
	print("b) This is not a even or odd function")
#Ex3_c
f= lambda x: x**2 +1
if even_function(x,f)== True:
	print("c) This is a enven function")
elif odd_function(x,f)== True:
	print("c) This is a odd function")
else :
	print("c) This is not a even or odd function")
#Ex3_d
f = lambda x: x**3+x
if even_function(x,f)== True:
	print("d) This is a enven function")
elif odd_function(x,f)== True:
	print("d) This is a odd function")
else :
	print("d) This is not a even or odd function")
#Ex3_e
f = lambda x: abs(x**3)
if even_function(x,f)== True:
	print("e) This is a enven function")
elif odd_function(x,f)== True:
	print("e) This is a odd function")
else :
	print("e) This is not a even or odd function")
#Ex3_f
f = lambda x: 2*x+1
if even_function(x,f)== True:
	print("f) This is a enven function")
elif odd_function(x,f)== True:
	print("f) This is a odd function")
else :
	print("f) This is not a even or odd function")
#Ex3_g
f = lambda x: x**4+3*(x**2)-1
if even_function(x,f)== True:
	print("g) This is a enven function")
elif odd_function(x,f)== True:
	print("g) This is a odd function")
else :
	print("g) This is not a even or odd function")
#Ex3_h
f = lambda x: 2*abs(x)+1
if even_function(x,f)== True:
	print("h) This is a enven function")
elif odd_function(x,f)== True:
	print("h) This is a odd function")
else :
	print("h) This is not a even or odd function")
x1 = 2
x2 = 5
def  increasing (f,x1,x2):
	if x1 < x2:
		if f(x1)<f(x2):
			return True
		else:
		 return False
def decreasing(f,x1,x2):
	if x1 < x2:
		if f(x1)>f(x2):
			return True
		else :
			return False
#Ex3_i
f = lambda x: -x**3
if increasing(f,x1,x2)==True:
	print ("i) is increasing")
elif decreasing(f,x1,x2)==True:
	print ("i) is decreasing")
else :
	print ("i) is not increasing or decreasing")
#Ex3_j
f= lambda x: -1/(x**2)
if increasing(f,x1,x2)==True:
	print ("j) is increasing")
elif decreasing(f,x1,x2)==True:
	print ("Ex3_j) is decreasing")
else :
	print ("j) is not increasing or decreasing")
#Ex3_k
f = lambda x: -1/x
if increasing(f,x1,x2)==True:
	print ("k) is increasing")
elif decreasing(f,x1,x2)==True:
	print ("k) is decreasing")
else :
	print ("k) is not increasing or decreasing")
#Ex3_l
f= lambda x: 1/abs(x)
if increasing(f,x1,x2)==True:
	print ("l) is increasing")
elif decreasing(f,x1,x2)==True:
	print ("l) is decreasing")
else :
	print ("l) is not increasing or decreasing")
#Ex3_m
f = lambda x: math.sqrt(abs(x))
if increasing(f,x1,x2)==True:
	print ("i) is increasing")
elif decreasing(f,x1,x2)==True:
	print ("i) is decreasing")
else :
	print ("i) is not increasing or decreasing")
#Ex3_n
f = lambda x : math.sqrt(abs(-x))
if increasing(f,x1,x2)==True:
	print ("i) is increasing")
elif decreasing(f,x1,x2)==True:
	print ("i) is decreasing")
else :
	print ("i) is not increasing or decreasing")

