class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LList:
    def __init__(self):
        self.head=None
    def print_(self):
        point=self.head
        while point is not None:
            print(point.data)
            point=point.next
my_ll=LList()

n2=Node("data2")
my_ll.head=Node("data1")
my_ll.head.next=n2
my_ll.print_()