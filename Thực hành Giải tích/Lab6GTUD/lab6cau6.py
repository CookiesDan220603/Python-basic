import sympy as sp 
import math 

n = sp.symbols('n')

#Ex6b 
a_n = n**3 / (n**3 + 1)
print("Limit of the sequence a_n - 6b is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6b is converged")
print("-----")

#Ex6c
a_n = (3 + 5 * pow(n, 2)) / (n + pow(n, 2))
print("Limit of the sequence a_n - 6c is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6c is converged")
print("-----")

#Ex6d
a_n = pow(n, 3) / (n + 1)
print("Limit of the sequence a_n - 6d is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6d is diverged")
print("-----")

#Ex6e
a_n = sp.exp(1 / n)
print("Limit of the sequence a_n - 6e is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6e is converged")
print("-----")

#Ex6f
a_n = sp.sqrt((n + 1) / (9 * n + 1))
print("Limit of the sequence a_n - 6f is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6f is converged")
print("-----")

#Ex6g
a_n = (pow(-1, n + 1) * n) / (n + sp.sqrt(n))
print("Limit of the sequence a_n - 6g is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6g is diverged")
print("-----")

#Ex6h
a_n = sp.tan((2 * n * sp.pi) / (1 + 8 * n))
print("Limit of the sequence a_n - 6h is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6h is converged")
print("-----")

#Ex6i
a_n  = sp.factorial(2 * n - 1) / sp.factorial(2 * n + 1)
print("Limit of the sequence a_n - 6i is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6i is converged")
print("-----")

#Ex6j
a_n = sp.log(2 * n*n + 1) - sp.log(n*n + 1)
print("Limit of the sequence a_n - 6j is:", sp.limit_seq(a_n, n))
print("The sequence a_n - 6j is converged")
print("-----")