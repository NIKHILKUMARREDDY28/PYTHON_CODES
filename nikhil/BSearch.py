
def BSearch(arr,ele,start,end):
    mid=(start+end)//2
    if(arr[mid]==ele):
        return mid
    if(ele>arr[mid]):
        BSearch(arr,ele,mid+1,end)
    else:
        BSearch(arr, ele, start, mid-1)
    return -1
arr=[int(x) for x in input().split()]
print("Enter The Value to Search")
ele=int(input())
start=0
end=len(arr)-1
BSearch(arr,ele,start,end)