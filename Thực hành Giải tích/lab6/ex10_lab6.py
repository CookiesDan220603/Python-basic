import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import math
y = 0
x = 0
d = 2
print("(a)")
anpha = 90
anpha_c = 0 #góc ban đầu
F = "F + F - F - F + F" #xét trường hợp n = 0
r0 = F
#Đổi từ độ sang radian
d2r = math.pi/180
n = 5
F_new = F
j = 0
while j<n: #n là số lần bạn muốn lặp
     F_new = F.replace("F",r0) #Tại những vị trí giá trị F thì sẽ thhay bằng r0
     F = F_new
     j += 1
#Vẽ hình
Px = [x]
Py = [y]

for i in F:
  if i == "F":
    x = x - d*math.cos(anpha_c * d2r)
    y = y - d*math.sin(anpha_c * d2r)
    Px.append(x)
    Py.append(y)
  elif i == "+":
    anpha_c = anpha_c + anpha
  elif i == "-":
    anpha_c = anpha_c - anpha
fg = plt.figure()
plt.plot(Px, Py, 'r')
plt.show()

#cau b
