n=int(input())
a=0
for i in range(1,n//2):
    t=i**2
    u=i**3
    z= t>u and t-u or u-t
    if z==n:
        print(i)


