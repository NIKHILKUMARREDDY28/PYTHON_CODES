def BS(arr,left,right,target):
    if left>right:
        return None
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return BS(arr,mid+1,right,target)
    else:
        return BS(arr,left,mid-1,target)
print(BS([1,5,7,8,9],0,4,8))