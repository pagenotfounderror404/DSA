class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
    def size(self, root):
        if root==None:
            return 0
        return self.size(root.left)+self.size(root.right)+1
def max_value(root):
    if root==None:
        return float("-inf")
    return max(root.data,max_value(root.left),max_value(root.right))
def left_view(root,level=1,maxlevel=0):
    if root==None:
        return
    if maxlevel<level:
        print(root.data, end=" ")
        maxlevel=level
    left_view(root.left,level+1,maxlevel)
    left_view(root.right,level+1,maxlevel)
t=Tree()
t.root=Node(8)
t.root.right=Node(1)
t.root.left=Node(6)
t.root.left.left=Node(9)
print(t.size(t.root))
print(max_value(t.root))
left_view(t.root)