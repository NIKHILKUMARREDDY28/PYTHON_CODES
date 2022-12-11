import math
def fun(i):
    dic = {10:'A',9:'B',8:'C',7:'D',6:'E+',5:'E',4:'F',3:'F',2:'F',1:'F',0:'F'}
    if i in dic:
        return dic[i]
def convertMarks(dici):
    for i in dici.keys():
        for j in dici[i].keys():
            dici[i][j] = fun(math.ceil(dici[i][j]/10))
    return dici

