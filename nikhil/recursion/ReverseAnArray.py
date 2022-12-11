arr =[1,2,3,4,5]
def func(l,r):
    if l > r:
        print(arr)
    else:
        arr[l],arr[r] = arr[r],arr[l]
        func(l+1,r-1)
func(0,4)
