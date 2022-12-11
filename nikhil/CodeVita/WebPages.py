class Solution:
    INF = 99999
    def __init__(self,mi):
        self.n=mi
        self.pager1=[[self.INF for x in range(mi)] for y in range(mi)]
    def Move(self,x,y):
        self.pager1[x][y]=1
    def Short(self,x,y):
        for via in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.pager1[i][j]=min(self.pager1[i][j],self.pager1[i][via] + self.pager1[via][j])
        if (self.pager1[x][y]==self.INF):
            return -1
        else:
            return self.pager1[x][y]
a=int(input())
obj=Solution(a)
for i in range(a):
    an=[int(x) for x in input().split()]
    for s in an:
        obj.Move(i,s-1)
c,d=map(int,input().split())
print(obj.Short(c-1,d-1))