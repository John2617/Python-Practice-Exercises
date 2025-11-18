import numpy as np
r=int(input("Enter a number of row : "))
c=int(input("Enter a number of column : "))
arr=[]
for i in range(r):
    s=input("Enter the entire row numbers separated by space: ")
    r=[]
    for j in s:
        r.append(int(j))
    arr.append(r)
org=np.array(arr)
print(org.astype(bool))
