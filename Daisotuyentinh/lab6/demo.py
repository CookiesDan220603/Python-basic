from cv2 import sqrt
import numpy as np
w = np.array([-1.-2,1,4])
##L1
##option 1
print(np.linalg.norm(w,1))
##option 2
print(sum(abs(w)))
print("------------------")
##L2
##option 1
print(np.linalg.norm(w,2))
##option 2
print(np.sqrt(sum(w**2)))
print("---------------------")
##Loo
##option 1
print(np.linalg.norm(w,np.inf))
##option 2
print(max(abs(w)))