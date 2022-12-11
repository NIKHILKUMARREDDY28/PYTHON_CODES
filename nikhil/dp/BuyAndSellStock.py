class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        l=0
        r=1
        maxi=0
        while r<n:
            if prices[l]<prices[r]:
                curr=prices[r]-prices[l]
                if curr>maxi:
                    maxi=curr
                r += 1
            else:
                l = r
                r = l + 1
        return maxi
obj=Solution()
lis=[int(x) for x in input().split(",")]
print(obj.maxProfit(lis))