def smallest(stock,valueK):
    #write your code here
    #a = stock.index(valueK)
    stock.sort()
    return stock[valueK-1]
lis = [10,5,7,88,19]
print(smallest(lis,3))