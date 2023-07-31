import numpy as np
x = np.array([1,4,12,1,6])
lst = x[::2]
lst = np.sort(lst)
print(lst)
lst1 =[]
for i in range(len(lst)):
    if (lst[i]%6 ==0):
        lst1.append(lst[i])
print(lst1)


