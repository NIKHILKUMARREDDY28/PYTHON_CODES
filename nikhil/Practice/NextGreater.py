def f(lis):
    n = len(lis)
    newlis = []
    for i in range(n):
        j = i
        while (  j < n and lis[i] >= lis[j]):
            j += 1
        if j == n or i == n-1:
            newlis.append(0)
        else:
            newlis.append(lis[j])
    return newlis
lis = [int(x) for x in input().split()]
print(f(lis))

