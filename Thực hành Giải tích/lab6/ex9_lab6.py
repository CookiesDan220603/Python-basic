#cau 10
def findFibo(i):
  if i < 1: return -1

  if i == 1: return 0
  if i == 2: return 1

  x1 = 0
  x2 = 1

  for k in range(3, i + 1):
    x_next = x2 + x1
    x1 = x2
    x2 = x_next

  return x_next

print( findFibo(8) )