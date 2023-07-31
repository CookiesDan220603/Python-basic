import numpy as np

a1 = 120
r = 0.5
f_n = lambda n: a1 * pow(r, n - 1)
a10 = f_n(10)
print(a10)

for i in np.arange(1, 101):
	if f_n(i) == 15 / 32:
		print("At n =", i,", f_n = 15/32")
		break
	if f_n(i) < 15 / 32:
		break