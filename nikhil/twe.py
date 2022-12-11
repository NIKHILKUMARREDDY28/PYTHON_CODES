A=[int(x) for x in input().split()]
D=int(input())
N=len(A)
if N%D==0:
    dec=D
else:
    dec=1
for i in range(dec):
    curr=i
    rep= (curr + D) % N
    temp=A[curr]
    while rep!=i :
        A[curr]=A[rep]
        #print(curr,rep)
        curr=rep
        rep= (curr + D) % N
    A[curr]=temp

    #nums[rep]=temp
print(A)