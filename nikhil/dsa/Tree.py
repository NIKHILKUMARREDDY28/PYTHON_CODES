class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def root_node(self,node):
        self.root=node
    def PrintT(self,root):
        if root:
            print(root.data)
            self.PrintT(root.left)
            self.PrintT(root.right)
bsr=BST()
one = Node(1)
bsr.root = one
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
bsr.root .left = two
bsr . root .right =three
two.left=four
two.right=five
bsr.PrintT(bsr.root)

