import numpy as np

a = np.array([(1,2,3),(4,5,6),(7,8,9)])
b = np.shape(a)
c = np.array(a).reshape(-1,3,3,1)
print(c.ndim,c)