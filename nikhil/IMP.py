l=[int(x) for x in input().split()]
d={}
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
for x,y in d.items():
    print(x,y)
