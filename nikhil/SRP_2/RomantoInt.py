def RomanInt(stri):
    con = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    num = 0
    if stri[0] in con:
        num = con[stri[0]]
    else:
        return "invalid"
    for i in range(1,len(stri)):
        if stri[i] in con:
            num += con[stri[i]]
            if con[stri[i]] > con[stri[i-1]]:
                num = num - 2 * con[stri[i-1]]
        else:
            return "invalid"
    return num
n = input()
print(RomanInt(n))