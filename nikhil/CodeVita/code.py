N,K = map(int,input().split())
lis = [int(x) for x in input().split()]
print(lis)
def Val(arr,target):
    curr= lis[0]
    l,r = 0,0
    while r<N:
        if curr == target:
            return [l+1,r+1]
        elif curr < target:
            r += 1
            curr += arr[r]
        elif curr > target:
            curr -= arr[l]
            l += 1
        print(curr)
    return -1
print(Val(lis,K))
