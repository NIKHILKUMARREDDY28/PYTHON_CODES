class Solution(object):
    def jump(self, nums):
        n = len(nums)
        currpos = 0
        count = 0
        left=currpos
        right=left+nums[left]
        while (currpos < n - 1 ):
            jump=0
            for i in range(left,right+1):
                if nums[i]>jump:
                    jump=nums[i]
                    currpos=i
            if jump>0:
                count+=1
            left=currpos
            right=currpos+nums[currpos]
            if right>n-1:
                right=n-1





        if currpos >= n - 1:
            return count
        else:
            return 0
obj=Solution()
nums=[int(x) for x in input().split(",")]
print(obj.jump(nums))