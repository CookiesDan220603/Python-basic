import numpy as np

E = np.array([[80, 98, 99, 85, 106, 94], 
            [71, 92, 76, 95, 100, 92], 
            [124, 163, 140, 160, 176, 161]])
A = np.array([[1, 2, 3], 
            [2, 1, 2],
            [3, 2, 4]])
def decodeMessage(a, E,AP ):
    a = np.dot(np.linalg.inv(a),E).T
    # print(a)
    a = np.round(a-4).astype(int)
    temp = ""
    for i in range(len(a)):
        for j in range(len(a[0])):
            temp += AP[a[i][j]]
    return temp

AP = list(map(chr, range(65, 91)))
AP.append(" ")
print(decodeMessage(A,E, AP))
