import itertools
class Solution(object):
    def twoSum(self, nums, target):
        nums1 = list(enumerate(nums))
        nums1=sorted(nums1,key=lambda x:x[1])
        l = 0
        n = len(nums1)
        r = n - 1
        while (l >= 0 and r <= n - 1):
            res = nums1[l][1] + nums1[r][1]
            if res == target:
                return [nums1[l][0] , nums1[r][0]]
            else:
                if res > target:
                    r -= 1
                elif res < target:
                    l += 1

obj=Solution()
print(obj.twoSum([3,2,4],6))