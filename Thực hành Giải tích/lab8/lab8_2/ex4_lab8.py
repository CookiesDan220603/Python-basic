from sympy import *
import matplotlib.pyplot as plt
import numpy as np
x = symbols('x')
def bai4(f,a,b):
  root = solve(diff(f,x,1))
  x_root = [a,b]
  for r in root:
    if r>=a and r<=b:
      x_root.append(r)
  x_root1 = np.unique(x_root) #bỏ đi phần tử trùng trong list
  f_root = []
  for r in x_root1:
    f_root.append(f.subs(x,r))
  print(f_root)
  Abs_max_i = np.argmax(f_root) #argmax trả về cho bạn vị trí của giá trị tối đa trong mảng
  Abs_min_i = np.argmin(f_root) #argmin trả về cho bạn vị trí của giá trị tối thiểu trong mảng
  print("Max = {} at x = {}".format(f_root[Abs_max_i],x_root1[Abs_max_i]))
  print("Min = {} at x = {}".format(f_root[Abs_min_i],x_root1[Abs_min_i]))
  fig = plt.figure()
  val = np.arange(a, b, 0.1)
  f_val = lambdify(x, f, "numpy")(val)
  plt.xlabel("0x")
  plt.xlabel("0y")
  plt.plot(val, f_val,'black')
  plt.plot(x_root1[Abs_max_i],f_root[Abs_max_i],'ro')
  plt.plot(x_root1[Abs_min_i],f_root[Abs_min_i],'*')
  plt.show()
bai4(x**2-2*x-5,0,2)
# bai4(3*x+x**3+5,-4,4)
# bai4(sin(x)+3*x**2,-2,2)
bai4(exp(x**2)+3*x,-1,1)
bai4(x**3-3*x,-3,0)
bai4(x**3-3*x,0,3)