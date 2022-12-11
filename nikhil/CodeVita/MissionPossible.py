class Solution:
    def __init__(self,x,y,n):
        self.maxi=0
        self.x=x
        self.y=y
        self.n=n
        self.score=0
        self.mylis = [[0 for i in range(n)] for j in range(n)]
        self.flag=True
    def is_valid(self,x,y):
        if x>=0 and x<=self.n-1 and y>=0 and y <= self.n - 1:
            return True
        return False
    def Change(self,x,y,point):
        if point>self.maxi:
            self.maxi=point
        self.mylis[x][y]=point
    def ans(self):
        if self.flag and self.score==self.maxi:
            return "*** Mission Passed! ***"+"\n"+"You have collected maximum points:"+str(self.score)
        return "*** Mission failed! ***"
    def Move(self,sa):
        if sa == 'L':
            self.x = self.x
            self.y = self.y - 1
            if self.is_valid(self.x,self.y):
                self.score += self.mylis[self.x][self.y] - 1
            else:
                self.flag=False
        elif sa == 'R':
            self.x = self.x
            self.y = self.y + 1
            if self.is_valid(self.x, self.y):
                self.score += self.mylis[self.x][self.y] - 1
            else:
                self.flag=False
        elif sa == 'U':
            self.x = self.x - 1
            self.y = self.y
            if self.is_valid(self.x, self.y):
                self.score += self.mylis[self.x][self.y] - 2
            else:
                self.flag=False
        elif sa == 'D':
            self.x = self.x + 1
            self.y = self.y
            if self.is_valid(self.x,self.y):
                self.score += self.mylis[self.x][self.y] - 2
            else:
                self.flag=False

        elif sa=='Q':
            print(self.score)
            print(self.ans())



a,b=map(int,input().split())
c,d=map(int,input().split(","))
myobj=Solution(c,d,a)
for i in range(a):
    e,f=map(int,input().split(","))
    poin=int(input())
    myobj.Change(e,f,poin)
str1=''
while str1!='Q':
    xo=input()
    str1=xo
    myobj.Move(str1)
