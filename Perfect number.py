n=int(input())
perfect=[]
for i in range(1,n+1):
    div=0
    for j in range(1,i):
        if i % j == 0:
            div+=j
    if div==i:
        perfect.append(i)
print(*perfect)