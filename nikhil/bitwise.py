class Move:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def south(self):
        self.i=self.i+1
        self.j=self.j
    def North(self):
        self.i=self.i-1
        self.j=self.j
    def east(self):
        self.i=self.i
        self.j=self.j+1
    def west(self):
        self.i=self.i
        self.j=self.j-1
    def pos(self):
        print("{}{}".format(self.i,self.j))
myobj=Move(1,1)
myobj.pos()
myobj.south()
myobj.pos()
myobj.west()
myobj.pos()
myobj.east()
myobj.pos()
