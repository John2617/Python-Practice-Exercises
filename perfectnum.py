def perfect(a):
    b=0
    for i in range(1,a//2+1):
        if a%i==0:
            b=b+i
    return b==a
num=int(input("Enter a number: "))#20
for z in range(1,num): #1,2,3,4,5....,19
    if perfect(z):
        print(z,end=',')
