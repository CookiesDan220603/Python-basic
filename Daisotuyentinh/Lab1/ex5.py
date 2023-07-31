import matplotlib.pyplot as plt
import numpy as np

lst = [1, 4, 6, 8, 22, 11, 10, 3, 6]

x = [str(i) for i in np.arange(len(lst))]
plt.bar(np.arange(len(lst)), lst, color = 'm')
plt.xticks(np.arange(len(lst)), x)
plt.show()