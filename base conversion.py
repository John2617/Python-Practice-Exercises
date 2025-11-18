n=int(input())
a=int(input())
result=0
place=1
while n>0:
    r=n%a
    result=r*place+result
    place*=10
    n//=a
print(result)