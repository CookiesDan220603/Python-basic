import matplotlib.pyplot as plt
import math 
import numpy as np
x= np.arange (0.1,4,0.01)
x1=1
y1=0
fx =lambda x: math.sin(10*math.pi / x)
y= list(map(fx,x))
plt.plot
value = [2,1.5,1.4,1.3,1.2,1.1,0.5,0.6,0.7,0.8,0.9]
for x2 in value:
	y2 = math.sin(10*math.pi / x2)
	slope = round((y2-y1)/(x2-x1),3)
	plt.title('slope = '+str(slope),fontsize=15,color='green')
	plt.plot(x,y,color='yellow')
	plt.plot([x1,x2],[y1,y2],color='green',label='PQ__')
	plt.plot(x1,y1,'bs')
	plt.plot(x2,y2,'rs')
	plt.grid(linestyle='--')
	plt.legend()
	plt.show()