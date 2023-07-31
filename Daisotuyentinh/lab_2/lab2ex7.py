import numpy as np

x = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])

## Ex7a
print("The maximize in vector x:", np.max(x, axis = 0))

## Ex7b
print("The minimize in vector x:", np.min(x, axis = 0))

## Ex7c
## print("Values bigger than 10:", x[x > 10])
print("The index of the values of x that are greater than 10:", np.nonzero(x > 10))

## Ex7d
print("Vector x after reversed:", x[::-1])

## Ex7e
print("Sort x vector in ascending order:", np.sort(x))

## Ex7f
print("Sort x vector in descending order:", np.sort(x)[::-1])

## Ex7g
count = 0
for i in range(0, len(x)):
    for j in range(i + 1, len(x)):
        if (x[i] + x[j] == 0):
            count += 1
print("The number of times xi + xj = 0 is:", count)

## Ex7h
count = 0
check_list = x.copy()
for i in range(0, len(x)):
    for j in range(i + 1, len(x)):
        if (x[i] == x[j]):
            check_list[j] = 0
for i in check_list:
    if (i == 0):
        count += 1
print("Total number of duplicate elements in x vector is:", count)

## Ex7i
y = []
n = len(x)
for i in range(0, len(x)):
    y.append(x[i] + x[n - i - 1])
print("Vector y =", np.array(y))

## Ex7j
def check_Armstrong_Number(n):
    temp = n
    sum = 0
    while (temp != 0):
        remainder = temp % 10
        sum += pow(remainder, 3)
        temp = int(temp / 10)
    if (sum == n):
        return True
    else:
        return False

w = []
for i in x:
    if check_Armstrong_Number(i) == True:
        w.append(i)
print("w =", np.array(w))

## Ex7k
lst = list (x)
for i in x:
    if (i < 0):
        lst.remove(i)
print("Vector x after delete all negative numbers:", np.array(lst))

## Ex7l
print("Median value in x vector:", np.median(x))

## Ex7m
sum = 0
ans = 0
for i in x: sum += i
mean_value = sum / (len(x))
for i in x:
    if (i < mean_value):
        ans += i
print("Sum of all values which are less than mean value in x vector:", ans)

## Ex7n
lst = list(x)
for i in np.arange(0, len(x)):
    if (lst[i] < 0):
        lst[i] = abs(lst[i])
print("New vector which each negative values is replaced by its absolute value:", np.array(lst))