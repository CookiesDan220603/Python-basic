import sympy as sp

x = sp.symbols('x')

#Ex 3a
fx = pow(x, 3) - 27 * x 
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 3a:")
print("Critical values:", c_val)
for i in c_val:
    if (i < 0) or (i > 5):
        c_val.remove(i)
c_val.extend([0, 5])

y_val = [fx.subs(x, v) for v in c_val] # Cấu trúc viết tắt trong Python
print("The absoluate maximum is:", max(y_val))
print("The absoluate minimum is:", min(y_val))
print("--------------")

#Ex 3b
fx = (3 / 2) * pow(x, 4) - 4 * pow(x, 3) + 4
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 3b:")
print("Critical values:", c_val)
for i in c_val:
    if (i < 0) or (i > 3):
        c_val.remove(i)
c_val.extend([0, 3])
y_val = [fx.subs(x, v) for v in c_val]
print("The absoluate maximum is:", max(y_val))
print("The absoluate minimum is:", min(y_val))
print("--------------")

#Ex 3c
fx = 0.5 * pow(x, 4) - 4 * pow(x, 2) + 5
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 3c:")
print("Critical values:", c_val)
for i in c_val:
    if (i < 1) or (i > 3):
        c_val.remove(i)
c_val.extend([1, 3])
y_val = [fx.subs(x, v) for v in c_val]
print("The absoluate maximum is:", max(y_val))
print("The absoluate minimum is:", min(y_val))
print("--------------")

#Ex 3d
fx = (5 / 2) * pow(x, 4) - (20 / 3) * pow(x, 3) + 6
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 3d:")
print("Critical values:", c_val)
for i in c_val:
    if (i < -1) or (i > 3):
        c_val.remove(i)
c_val.extend([-1, 3])
y_val = [fx.subs(x, v) for v in c_val]
print("The absoluate maximum is:", max(y_val))
print("The absoluate minimum is:", min(y_val))
print("--------------")