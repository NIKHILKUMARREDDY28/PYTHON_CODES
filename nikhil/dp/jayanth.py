res=[]
ind=[]
def pal(s,l,r):
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        if r - l > 0:
            for k in range(l + 1):
                res.append(s[k:r + 1])
                ind.append(str(k)+" "+str(r))

            for k in range(r + 1, len(s)):
                res.append(s[l:k + 1])
                ind.append(str(l) + " " + str(k))
        l -= 1
        r += 1
def pals(s):
    count=0
    for i in range(len(s)):
        pal(s,i,i)
        pal(s,i,i+1)
    print(res)
    print(ind)
    return len(set(ind))
n=input()
print(pals(n))