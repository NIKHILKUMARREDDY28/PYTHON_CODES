class Solution:
    def canPartition(self, nums) :
        def FunUtil(arr, ind, suma, dp):
            if suma == 0:
                return True
            if ind == 0:
                if suma == arr[ind]:
                    return True
                return False
            if dp[ind][suma] != -1:
                return dp[ind][suma]

            if suma >= arr[ind]:
                take = FunUtil(arr, ind - 1, suma - arr[ind], dp)
            else:
                take = False
            notTake = FunUtil(arr, ind - 1, suma, dp)
            dp[ind][suma] = take or notTake
            print(take or notTake)
            return dp[ind][suma]

        TotalSum = sum(nums) // 2
        if TotalSum % 2 != 0:
            return False
        indi = len(nums)
        dp = [[-1 for i in range(TotalSum)] for j in range(indi)]
        ans = FunUtil(nums, indi - 1, TotalSum, dp)
        print(dp)
        return ans



obj = Solution()
print(obj.canPartition([1,5,11,5]))