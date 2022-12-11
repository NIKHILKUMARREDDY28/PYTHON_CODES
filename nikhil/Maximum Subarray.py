import sys
class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        start=0
        max_sum=0
        curr_sum=0
        end=0
        while start<=n-1:
            curr_sum=sum(nums[start:end+1])

            if curr_sum >max_sum:
                max_sum=curr_sum
            if end==n-1:
                start+=1
                end=start
            end+=1
        return max_sum
mylis=[int(x) for x in input().split(",")]
sol=Solution()
print(sol.maxSubArray(mylis))