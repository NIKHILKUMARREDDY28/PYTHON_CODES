def helloganesh(n):
    if(n==1 or n==2):
        print((n-1)+3,end="")
        return
    n=n-1
    helloganesh(n//2)
    print((n%2)+3,end="")
n=12
helloganesh(n)