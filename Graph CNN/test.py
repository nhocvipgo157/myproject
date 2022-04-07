import numpy as np

A =np.array([[1,2,1,4],[2,1,3,4],[3,1,1,1],[4,5,1,1]])
print(len(A))
print(A)
for x in range (0,len(A)-1):
    for y in range (0,len(A)-1):
        if A[x][y+1] == A[x][y]:
            print('same')
        else:
            print("none")
