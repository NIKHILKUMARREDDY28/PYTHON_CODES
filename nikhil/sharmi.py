MOD = pow(10,9)+7

dp = [[[0 for i in range(101)]
       for i in range(101)]
      for i in range(101)]
N, M, K =0,0,0
def Initialize():
    for i in range(101):
        for j in range(101):
            for z in range(101):
                dp[i][j][z] = -1


# Function returns the total count
def CountWays(i, j, k):
    if (i >= N or i < 0 or
            j >= M or j < 0 or k < 0):
        return 0

    if (i == 0 and j == 0 and k == 0):
        return 1

    if (dp[i][j][k] != -1):
        return dp[i][j][k]
    else:
        dp[i][j][k] = (CountWays(i + 1, j, k - 1) +
                       CountWays(i - 1, j, k - 1) +
                       CountWays(i, j - 1, k - 1) +
                       CountWays(i, j + 1, k - 1) +
                       CountWays(i, j, k - 1) )
    return dp[i][j][k]


# Driver code
if __name__ == '__main__':
    N = 3
    M = 3
    n=int(input())
    ans=0
    for i in range(n):
        a=int(input())
        Initialize()
        ans+=((CountWays(0, 0, a)-1)*125000001)
print(ans)
