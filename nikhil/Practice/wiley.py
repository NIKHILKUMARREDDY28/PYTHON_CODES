
def f(st):
    n = len(st)
    if (st[-1] >= '0' and st[-1] <= '9'):
        if st[-1] == str(n)[-2] :
            return (n-1)%10
        return -1
    else:
        if len(str(n)) > 1:
            return -1
        return n

stri = input()
print(f(stri))
