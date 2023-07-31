import numpy as np 
def fib(n):
    if n < 2 :
        return n
    return fib(n-2) + fib(n-1)
#1a
fn = lambda n : 4*n + 1
n_array = np.arange(0,10)
x_n = list(map(fn,n_array))
print("Exercise 1a :")
print(x_n)
#1b
fn = lambda n: pow(n, 3)
n_array = np.arange(0,10)
x_n = list(map(fn, n_array))
print("Exercise 1b:")
print(x_n)

#1c
fn = lambda n: pow(3, n)
n_array = np.arange(0,10)
x_n = list(map(fn, n_array))
print("Exercise 1c:")
print(x_n)
#1d 
x_a =[]
for c in range (2,10):
	x_a.append(fib(c))
print("Exercise 1d:")
print(x_a)


