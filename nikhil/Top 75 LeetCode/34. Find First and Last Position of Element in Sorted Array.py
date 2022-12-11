import sys
def coinchange(coins,sum):
    dp=[sys.maxsize] * (sum+1)
    dp[0]=0
    for i in range(1,sum+1):
        for j in coins:
            if i-j >= 0 :
                dp[i]=min(1+dp[i-j],dp[i])
    return dp[sum]
print(coinchange([1,2,5],11))
