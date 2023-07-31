import sympy as sp 
import math

n = sp.symbols('n')

#Ex9a
series_9a = sp.Sum(4 ** n, (n, 1, sp.oo))

converged = series_9a.is_convergent()

if converged:
	print("The sequence 9a is converged")
else:
	print("The sequence 9b is not converged")

print("------------------------------")
#Ex9b
series = sp.Sum(5 / 2**n, (n, 1, sp.oo))

converged = series.is_convergent()

if converged:
	print("The sequence 9b is converged")
else:
	print("The sequence 9b is not converged")