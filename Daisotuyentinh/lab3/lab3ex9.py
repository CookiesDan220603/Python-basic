import numpy as np

T = np.array([[0.6, 0.7], [0.4, 0.3]])
p = np.array([[0.5], [0.5]])

## k = 1
pk = T @ p
print("With k = 1, pk =")
print(pk)

## k = 2
pk = (T @ T) @ p
print("With k = 2, pk =")
print(pk)

## k = 10
k = 10
temp = T
for i in range(1, k + 1):
    temp = temp @ T
pk = temp @ p
print("With k = 10, pk =")
print(pk)

## k = 100
k = 100
temp = T
for i in range(1, k + 1):
    temp = temp @ T
pk = temp @ p
print("With k = 100, pk =")
print(pk)

## k = 100000
k = 100000
temp = T
for i in range(1, k + 1):
    temp = temp @ T
pk = temp @ p
print("With k = 100000, pk =")
print(pk)
print("--- End ---")