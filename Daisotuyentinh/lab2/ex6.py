import numpy as np



x = np.arange(0, 22, 2)

## Ex6a
print("The first sixth elements in vector x:", x[:6])

## Ex6b
print("The last fifth elements in vector x:", x[-5:])

## Ex6c
print("The first, fourth,  last fourth elements in vector x:", x[np.array([0,3,-1])])


## Ex6d
print("The first, third, fifth, seventh elements in vector x:", x[1:8:2])

## Ex6e

print("The elements with the odd indices in the vector x:", x[1::2]) 

## Ex6f
lst = []
for i in np.arange(0, 12, 2):
    lst.append(x[i])
print("The elements with the even indices in the vector x:", x[::2])