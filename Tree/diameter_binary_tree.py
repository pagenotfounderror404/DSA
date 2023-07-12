class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
def height(root):
    if root==None:
        return 0
    return max(height(root.left),height(root.right))+1
def diameter(root):
    if root==None:
        return 0
    d1=1+height(root.left)+height(root.right)
    d2=diameter(root.left)
    d3=diameter(root.right)
    return max(d1,d2,d3)
def diameter_efficient(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    diameter_efficient.res=max(diameter_efficient.res,1+lh+rh)
    return (1+max(lh,rh))
t=Tree()
t.root=Node(8)
t.root.right=Node(2)
t.root.left=Node(6)
t.root.left.left=Node(6)
print(diameter(t.root))