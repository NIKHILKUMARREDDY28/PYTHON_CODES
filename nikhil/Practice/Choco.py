def func(stri,arr):
    n = len(stri)
    dic = {}
    for i in range(n):
        if stri[i] in dic:
            dic[stri[i]] = max(dic[stri[i]],arr[i])
        else:
            dic[stri[i]] = arr[i]
    return sum(arr) - sum(dic.values())
print(func('amid',[9,0,8,2]))