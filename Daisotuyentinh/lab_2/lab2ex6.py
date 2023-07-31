import numpy as np



x = np.arange(0, 22, 2)

## Ex6a
print("The first sixth elements in vector x:", x[5])

## Ex6b
print("The last fifth elements in vector x:", x[-5])

## Ex6c
print("The first fourth elements in vector x:", x[3])
print("The last fourth elements in vector x:", x[-4])

## Ex6d
print("The first third elements in vector x:", x[2])
print("The first fifth elemenst in vector x:", x[4])
print("The first seventh elements in vector x:", x[6])

## Ex6e
lst = [] 
for i in np.arange(1, 10, 2):
    lst.append(x[i])
print("The elements with the odd indices in the vector x:", np.array(lst)) 

## Ex6f
lst = []
for i in np.arange(0, 12, 2):
    lst.append(x[i])
print("The elements with the even indices in the vector x:", np.array(lst))