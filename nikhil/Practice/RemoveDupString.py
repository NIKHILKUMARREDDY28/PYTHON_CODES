def f(sty):
    res = ""
    for i in range(len(sty)):

        if sty[i] not in res:
            res += sty[i]
    return res
n = input()
print(f(n))