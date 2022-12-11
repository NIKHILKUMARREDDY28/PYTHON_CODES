import sys

def coin(ind,arr,target):
    take=0
    nottake=0

    if ind<0:
        return 0
    if target==0:
        return 1
    if arr[ind]>target:
        coin(ind-1,arr,target)
    else:
        take = 1 +coin(ind,arr,target-arr[ind])
        nottake =coin(ind-1,arr,target)
        return min(take,nottake)
    return -1
arr1=[int(x) for x in input().split()]
print(coin(len(arr1)-1,arr1,11))