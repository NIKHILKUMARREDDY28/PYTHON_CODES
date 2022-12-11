n=int(input())
prices=[]
order=[]
for i in range(n):
    prices.append(int(input()))
a=1
while(a!=len(prices)):
    if prices[a]<prices[a-1]:
        order.append(prices[a])
    a+=1
order.sort()
print(order)
for i in range(len(prices)):
    res=1
    b=0
    while(prices[i]<order[b]):
        res+=1
    print(res)



