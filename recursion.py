def fun(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fun(n-1) + fun(n-2)+fun(n-3)
n=int(input())
print(fun(n))