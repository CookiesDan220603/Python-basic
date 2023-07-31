import math
## a) f(X)= x**(1/2)
def exponential_fucntion_a(x):
  return math.sqrt(x)
x=4
out= exponential_fucntion_a(x)
print ("a) f(x)= {}".format(out))
print ("---------------")
## b) f(x) = x**(1/3)
def exponential_fucntion_b(x):
  return x**(1/3)
out= exponential_fucntion_b(x)
print("b) f(x)= {}".format(out))
print ("---------------")
## (c) f(x) = x**(2/3)
def exponential_fucntion_c(x):
  return x**(2/3)
out= exponential_fucntion_c(x)
print("b) f(x)= {}".format(out))
print ("---------------")
## (d) f(x) = 1/3(x**3)-1/2(x**2)-2*x+1/3
def polynomial_fuctions_d (x):
  return (1/3*(x**3) - 1/2*(x**2) - 2*x + 1/3)
out = polynomial_fuctions_d(x)
print("d) f(x)= {}".format(out))
print ("---------------")
## e) f(x)= (2*(x**2)-3)/(7*x+4)
def polynomial_fuctions_e (x):
  return (2*(x**2)-3)/(7*x+4)
out = polynomial_fuctions_e(x)
print ("e) f(x) = {}".format(out))
print ("---------------")
## f) f(x)= (5*(x**2)+8*x -3)/(3**2 + 2)
def polynomial_fuctions_f (x):
  return (5*(x**2)+8*x -3)/(3**2 + 2)
out = polynomial_fuctions_f(x)
print ("f) f(x) = {}".format(out))
print ("---------------")
##(g) f(x) = sin(x)
def Trigonometric_Functions_g(x):
  return math.sin(x)
out = Trigonometric_Functions_g(x)
print ("g) f(x) = {}".format(out))
print ("---------------")
##(h) f(x) = cos(x)
def Trigonometric_Functions_h(x):
  return math.cos(x)
out = Trigonometric_Functions_h(x)
print ("h) f(x) = {}".format(out))
print ("---------------")
##(i) f(x) = 3**x
def polynomial_fuctions_i (x):
  return 3**x
out= polynomial_fuctions_i(x)
print ("i) f(x) = {}".format(out))
print ("---------------")
##(j) f(x) = 10**(-x)
def polynomial_fuctions_j (x):
  return 10**(-x)
out= polynomial_fuctions_j(x)
print ("j) f(x) = {}".format(out))
print ("---------------")
##(k) f(x) = e**x
def polynomial_fuctions_k (x):
  return math.exp(x)
out= polynomial_fuctions_k(x)
print ("k) f(x) = {}".format(out))
print ("---------------")
## (l) f(x) = log2(x)
def Logarithmic_Functions_l (x):
  return math.log2(x)
out= Logarithmic_Functions_l(x)
print ("l) f(x) = {}".format(out))
print ("---------------")
##(m) f(x) = log10(x)
def Logarithmic_Functions_m (x):
  return math.log10(x)
out= Logarithmic_Functions_m(x)
print ("m) f(x) = {}".format(out))
print ("---------------")
##(n) f(x) = ln(x)
def Logarithmic_Functions_n (x):
  return math.log(x)
out= Logarithmic_Functions_n(x)
print ("m) f(x) = {}".format(out))
print ("---------------")