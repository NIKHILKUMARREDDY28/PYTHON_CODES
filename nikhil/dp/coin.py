class Solution(object):
    dp=[]
    def Initialize(self,x,y):
        self.dp=[[-1 for i in range(y+1)]for j in range(x)]


    def coinChange(self, coins, idx, amount):

        if amount == 0:
            return 0
        if idx < 0:
            return -1

        if amount < coins[idx]:
            self.dp[idx][target] = self.coinChange(coins, idx - 1, amount)
        else:
            self.dp[idx][target] = 1 + self.coinChange(coins, idx, amount - coins[idx])
        return self.dp[idx][target]



obj = Solution()

coins = [int(x) for x in input("Enter coin denom").split()]
target = int(input("Enter Target"))
coins.sort()
obj.Initialize(len(coins),target)
print(obj.coinChange(coins, len(coins) - 1, target))
print(obj.dp)