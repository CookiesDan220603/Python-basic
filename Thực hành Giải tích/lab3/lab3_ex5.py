import math 
import numpy as np
from sympy import *

x = symbols('x')

#Ex5_a
fx_5a = x*x - 7
lim_5a = limit(fx_5a, x, 1)
limr_5a = limit(fx_5a,x,1,'+')
liml_5a = limit(fx_5a,x,1,'-')
print ("Gioi han trai f(x) = {}".format(liml_5a))
print ("Gioi han phai f(x) = {}".format(limr_5a))
print ("Gioi han tai diem a f(x) = {}".format(lim_5a))
if (lim_5a==limr_5a and lim_5a==liml_5a):
	print("f(x) lien tuc tai diem c=1")
else :
	print("f(x) khong lien tuc tai diem c=1")

#Ex_5b
fx_5b = pow(2*x - 3, 1/2)
lim_5b = limit(fx_5b, x, 2)
limr_5b = limit(fx_5b,x,2,'+')
liml_5b = limit(fx_5b,x,2,'-')
print ("Gioi han trai f(x) = {}".format(liml_5b))
print ("Gioi han phai f(x) = {}".format(limr_5b))
print ("Gioi han tai diem a f(x) = {}".format(lim_5b))
if (lim_5b==limr_5b and lim_5b==liml_5b):
	print("f(x) lien tuc tai diem c=1")
else :
	print("f(x) khong lien tuc tai diem c=2")