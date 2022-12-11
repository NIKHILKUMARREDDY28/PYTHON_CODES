from itertools import combinations
n = int(input())
r = int(input())
l = list(map(str, input().split(',')))

new = []
new.append('')
for i in range(1,len(l)+1):
    c = combinations(l,i)
    for i in c:
        new.append(list(i))

ss = new[r-1]
le = len(ss)
for i in range(le):
    if(i==le-1):
        print(ss[i])
    else:
        print(ss[i], end="")
        print(',', end="")