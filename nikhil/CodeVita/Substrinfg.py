arr = [1,2,3,5,4,6,7,8]
n = len(arr)
ans = [0] * n
ans2 = [0]* n
ans2[n-1] =  1
ans[0] = 1
for i in range(1,n):
    if(arr[i] > arr[i-1]):
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = 0
for i in range(n-2,-1,-1):
    if (arr[i] > arr[i+1]):
        ans2[i] = ans2[i+1] + 1
    else:
        ans2[i] = 0
print(ans)
print(ans2)

