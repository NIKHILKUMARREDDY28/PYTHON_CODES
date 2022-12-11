from collections import Counter
N=int(input())
a=[int(x) for x in input().split()]
print(sum(1 for c in Counter(a).values() if c == 1))