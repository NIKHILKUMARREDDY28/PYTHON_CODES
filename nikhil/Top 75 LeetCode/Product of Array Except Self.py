class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        r=1
        l=1
        for i in range(len(nums)):
            res[i]*=l
            res[-(i+1)]*=r
            l*=nums[i]
            r*=nums[-(i+1)]
        return res
nums=[int(x) for x in input().split(",")]
obj1=Solution()
print(obj1.productExceptSelf(nums))