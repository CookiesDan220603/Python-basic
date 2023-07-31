import sympy as sp
import matplotlib.pyplot as plt
#funtion a
def ex7a(f,x,x0):
    h = sp.symbols('h')
    q = ( f.subs(x,x0+h) -f.subs(x,x0) )/h
    lm = sp.limit(q , h , 0 )
    print ("The limit of function q as h -> 0 =",lm)
    y1= f.subs(x,x0) +q.subs(h,3)*(x)
    y2= f.subs(x,x0) +q.subs(h,2)*(x)
    y3= f.subs(x,x0) +q.subs(h,1)*(x)
    sp.plot(f,y1,y2,y3,(x,-1/2,3))
    

    
#ex7_a
x = sp.symbols('x')
f = x**3 + 2*x
ex7a(f, x, 0)

#function b

def ex7b(f,x,x0):
    h = sp.symbols('h')
    q = ( f.subs(x,x0+h) -f.subs(x,x0) )/h
    lm = sp.limit(q , h , 0 )
    print ("The limit of function q as h -> 0 =",lm)
    y1= f.subs(x,x0) +q.subs(h,3)*(x-1)
    y2= f.subs(x,x0) +q.subs(h,2)*(x-1)
    y3= f.subs(x,x0) +q.subs(h,1)*(x-1)
    sp.plot(f,y1,y2,y3,(x,0.5,4,0.1))

    
#main
#7b
f = x + 5/x
ex7b(f, x, 1)

#dunction c
def ex7c(f,x,x0):
    h = sp.symbols('h')
    q = ( f.subs(x,x0+h) -f.subs(x,x0) )/h
    lm = sp.limit(q , h , 0 )
    pi = sp.pi
    print ("The limit of function q as h -> 0 =",lm)
    y1= f.subs(x,x0) +q.subs(h,3)*(x-pi/2)
    y2= f.subs(x,x0) +q.subs(h,2)*(x-pi/2)
    y3= f.subs(x,x0) +q.subs(h,1)*(x-pi/2)
    sp.plot(f,y1,y2,y3,(x,pi/2-1/2,pi/2+3,0.1))

    
#main
#7c
f = x + sp.sin(2*x)
ex7c(f, x, sp.pi/2)


#funtion d
def ex7d(f,x,x0):
    h = sp.symbols('h')
    q = ( f.subs(x,x0+h) -f.subs(x,x0) )/h
    lm = sp.limit(q , h , 0 )
    pi = sp.pi
    print ("The limit of function q as h -> 0 =",lm)
    y1= f.subs(x,x0) +q.subs(h,3)*(x-pi)
    y2= f.subs(x,x0) +q.subs(h,2)*(x-pi)
    y3= f.subs(x,x0) +q.subs(h,1)*(x-pi)
    sp.plot(f,y1,y2,y3,(x,pi-1/2,pi+3,0.1))

    
#main
#7b
f = sp.cos(x) + 4*sp.sin(2*x)
ex7d(f, x, sp.pi)

