import numpy as np
arr=np.array([[10,20,30],[50,20,80],[30,80,70]])
row=np.mean(arr,axis=0)
col=np.mean(arr,axis=1)
res=np.array([row,col])
print(res)
