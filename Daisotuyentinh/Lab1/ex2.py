import numpy as np
a = {0: 1, 1: 2, 2: 3, 3: 4}
b =[]
for k in a.keys():
	b.append(a[k])
c = tuple(b)
d = set(b)
print(a)
print(b)
print(c)
print(d)
