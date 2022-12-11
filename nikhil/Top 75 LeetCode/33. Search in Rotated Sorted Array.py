class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while (l<=r):
            mid = l + (r - l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[l] :
                if nums[mid] < target:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target > nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
obj=Solution()
print(obj.search([3,5,1],3))