import numpy as np
arr=np.array([[78,29,31],[57,83,91],[31,83,79]])
row=np.min(arr,axis=0)
col=np.sort(arr,axis=1)
res=np.array([row,col])
print(res)
