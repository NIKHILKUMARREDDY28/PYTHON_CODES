class Solution(object):


    def coinChange(self, coins, idx, amount):
        num=0
        coins.sort()

        if amount==0:
            return 0
        if idx<0:
            return -1

        if amount<coins[idx]:
            return self.coinChange(coins,idx-1,amount)

        return 1+self.coinChange(coins,idx,amount-coins[idx])

obj=Solution()
coins=[int(x) for x in input("Enter coin denom").split()]
target=int(input("Enter Target"))
print(obj.coinChange(coins,len(coins)-1,target))