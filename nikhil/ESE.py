n = int(input())
x = [int(x) for x in input().split()]
def minmax(x, i,min,max):
    if (i == len(x) - 1):
        return max - min
    else:
        if (x[i] < x[min]):
            min = i
        elif (x[i] > x[max]):
            max = i
        return minmax(x, i + 1,min,max)
print(minmax(x, 1,0,0))
