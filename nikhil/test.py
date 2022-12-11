T=int(input())
for i in range(T):
  n,k=map(int,input().split())
  dic={}
  dic=dict([input().split() for i in range(n)])
  dict1=sorted(dic.items(), key =lambda kv:(kv[1], kv[0]))
  for x in range(k):
      print(dict1[x][0],end=" ")