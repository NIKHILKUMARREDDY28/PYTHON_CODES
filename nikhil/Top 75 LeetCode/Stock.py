
class Solution(object):
    def maxProfit(self, prices):

        n=len(prices)
        res=0
        minl=prices[0]
        maxr=prices[n-1]
        l=1
        r=n-2
        while r>=l:
            while prices[r]>maxr and r>=l:
                r-=1

            while prices[l]<minl and l<=r:
                l+=1

            if prices[l]<prices[r]:
                curr=prices[r]-prices[l]
                if res<curr:
                    res=curr
        return res




a=[int(x) for x in input().split()]
obj=Solution()
print(obj.maxProfit(a))