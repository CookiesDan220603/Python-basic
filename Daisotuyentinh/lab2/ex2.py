import numpy as np
def SNT(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
 
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
#ex2a
n = int(input("Enter n value :"))
ex2a = []
for i in range(n):
    ex2a.append(12 + 2*i);
ex2a_vector = np.array(ex2a)
print("Exercise 2a : ")
print(ex2a_vector)
print("*****************")
#ex2b
ex2b = []
for i in range(n):
    ex2b.append(31 + 2*i);
ex2b_vector = np.array(ex2b)
print("Exercise 2b : ")
print(ex2b_vector)
print("*****************")
#ex2c
ex2c = []
for i in np.arange(-n,n+1,1):
    ex2c.append(i)
ex2c_vector = np.array(ex2c)
print("Exercise 2c :")
print(ex2c_vector)
print("****************")
#ex2d
ex2d_vector = ex2c_vector[::-1]
print("Exercise 2d :")
print(ex2d_vector)
print("****************")
#ex2e
ex2e =[10,8,6,4,2,0,-2-4]
ex2e_vector = np.array(ex2e)
print("Exercise 2e")
print(ex2e_vector)
print("*****************")
#ex2f
ex2f = []
for i in np.arange(1,n+1,1):
    ex2f.append(1/(2**i))
ex2f_vector = np.array(ex2f)
print("Exercise 2f")
print(ex2f_vector)
print("*****************")
#ex2g
ex2g = []
for i in np.arange(1,n+1,1):
    if (SNT(i)== True):
        ex2g.append(i)
ex2g_vector = np.array(ex2g)
print("Exercise 2g")
print(ex2g_vector)
print("*****************")
#ex2h
ex2h = []
for i in np.arange(1,n+1,1):
    ex2h.append(1/fibonacci(i))
ex2h_vector = np.array(ex2h)
print("Exercise 2h")
print(ex2h_vector)
print("*****************")
#ex2i
ex2i = [1]
for i in np.arange(1,n+1,1):
    ex2i.append( ex2i[i-1] + i +1)
    
ex2i_vector = np.array(ex2i)
print("Exercise 2i")
print(ex2i_vector)
print("*****************")
#ex2j
ex2j =[]
k =2
for i in np.arange(3,n*2 + 1,2):
    ex2j.append(1/k)
    k += i
    
ex2j_vector = np.array(ex2j)
print("Exercise 2j")
print(ex2j_vector)
print("*****************")
#ex2k
ex2k =[0]
for i in range(1,n):
    ex2k.append(i/(i+1))
    
ex2k_vector = np.array(ex2k)
print("Exercise 2k")
print(ex2k_vector)
print("*****************")
#ex2l
ex2l = []
a = ord('a')
z = ord('z')
vector_o = np.arange(a, z + 1, 1)
for i in vector_o:
    ex2l.append(chr(i))
print("Exercise 2l")
print("Vector o =", np.array(ex2l))
print("*****************")
#ex2m
ex2m = []
a = ord('A')
z = ord('Z')
vector_s = np.arange(a, z + 1, 3)
for i in vector_s:
    ex2m.append(chr(i))
print("Exercise 2m")
print("Vector s =", np.array(ex2m))
print("--- End ---")
