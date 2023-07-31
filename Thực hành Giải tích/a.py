import math
from sympy import *
#a) f(x)= sqrt(|x|)
x0=symbols('x')
f = sqrt(abs(x0))
plot(f,(x0, -4, 4),show = True)
plot (f,(x0, -4,4),line_color ='green',title= "F(x) = sqrt(|x|",show=True)