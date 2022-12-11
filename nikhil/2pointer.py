def Arra(arr,k):
    i=0
    n=len(arr)
    j=n-1
    while(i<n and j>0):
        if (arr[i]+arr[j]==k):
            return (i,j)
        elif arr[i]+arr[j]>k:
            j -= 1
        elif arr[i]+arr[j]<k:
            i += 1
n=[int(x) for x in input().split(",")]
a=int(input())
print(Arra(n,a))