import numpy as np

## Exercise 2a

n = int(input("Enter n: "))
lst_2a = []
print("Exercise 2a:")
vector_b = np.arange(12, 12 + 2 * n, 2)
print("Vector b =", vector_b)

## Exercise 2b

lst_2b = []
print("Exercise 2b:")
vector_c = np.arange(31, 31 + 2 * n, 2)
print("Vector c =", vector_c)

## Exercise 2c
lst_2c = []
print("Exercise 2c:")
vector_x = np.arange(-n, n + 1, 1)
print("Vector x =", vector_x)

## Exericse 2d
print("Exercise 2d:")
vector_y = np.arange(-n, n + 1, 1)
print("Vector y =", vector_y[::-1])

## Exercise 2e
print("Exercise 2e:")
lst_2e = []
while (n > 8):
    print("The number you just entered is invalid, please enter again: ")
    n = int(input())
if (n <= 8):
    vector_z = np.arange(10 - 2*n + 2, 10 + 1, 2)
print("Vector z =", vector_z[::-1])

## Exercise 2f
print("Exercise 2f:")
vector_w = 1 / (2 ** np.arange(n))
print("Vector w =", vector_w)

## Exercise 2g
lst_d = [1, 1]

vector_d = 1 / np.array([np.round((1.618 ** i - (1 - 1.618) ** i) / np.sqrt(5)) for i in np.arange(1, n + 1)])
print("Vector d =", vector_d)

## Exercise 2i
print("Exercise 2i:")
lst = []
first_element = 1
k = 2
for i in range (0, n):
    lst.append(first_element)
    first_element += k
    k += 1
vector_a = np.array(lst)
print("Vector a =", vector_a)

## Exercise 2j
print("Exercise 2j:")
lst = []
k = 2
foot_step = 3
for i in range(0, n):
    lst.append(1 / k)
    k += foot_step
    foot_step += 2
vector_n = np.array(lst)
print("Vector n =", vector_n)

## Exercise 2k
print("Exercise 2k:")
lst = []
k = 1
for i in range(0, n):
    lst.append(i / k)
    k += 1
vector_p = np.array(lst)
print("Vector p =", vector_p)

## Exercise 2l
lst = []
a = ord('a')
z = ord('z')
vector_o = np.arange(a, z + 1, 1)
for i in vector_o:
    lst.append(chr(i))
print("Vector o =", np.array(lst))

## Exercise 2m
lst = []
a = ord('A')
z = ord('Z')
vector_s = np.arange(a, z + 1, 3)
for i in vector_s:
    lst.append(chr(i))
print("Vector s =", np.array(lst))
print("--- End ---")