from math import *
a,b=map(int,input().split())

def sum(a,b):
    sum1=0
    while(a>0):
        m=a%10
        n=b%10
        sum1=sum1+abs(m-n)
        a=a//10
        b=b//10
    return  sum1
mysum=0
for i in range(a,b+1):
    for j in range(i+1,b+1):
        mysum+=sum(i,j)
print(mysum)

