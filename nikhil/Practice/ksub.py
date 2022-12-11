from itertools import  combinations
def f(nums,k):
    ans = [len(set(x)) for x in combinations(nums,k)]
    return min(ans)
arr = [1,3,2,4,3,4,5,3,4,3]
print(f(arr,6))