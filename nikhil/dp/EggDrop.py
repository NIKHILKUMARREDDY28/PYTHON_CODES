import sys
def EggDrop(eggs,floor):
    dp = [[sys.maxsize for i in range(eggs+1)]for j in range(floor+1)]

    if floor == 1 or floor == 0:
        return floor
    if eggs==1:
        return floor
    for x in range(1, floor + 1):
        if dp[floor][eggs]
        res = max(EggDrop(eggs - 1 , x - 1 ),EggDrop(eggs,floor - x))
        if (res < min):
            min = res
    return dp[floor][eggs]
print(EggDrop(2,10))