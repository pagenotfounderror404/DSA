from collections import deque
class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
def children_sum_property(root):
    if root==None:
        return True
    if root.left==None and root.right==None:
        return True
    sum=0
    if root.left!=None:
        sum+=root.left.data
    if root.right!=None:
        sum+=root.right.data
    return root.data==sum and children_sum_property(root.left) and children_sum_property(root.right)

def height(root):
    if root==None:
        return 0
    return max(height(root.left),height(root.right))+1
def balanced_tree(root):
    if root==None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    return abs(lh-rh)<=1 and balanced_tree(root.left) and balanced_tree(root.right)
def max_width(root):
    if root==None:
        return 0
    q=deque()
    maxwidth=0
    q.append(root)
    while q:
        count=len(q)
        maxwidth=max(count,maxwidth)
        while count!=0:
            count-=1
            temp=q.popleft()
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
    return maxwidth


t=Tree()
t.root=Node(8)
t.root.right=Node(2)
t.root.left=Node(6)
t.root.left.left=Node(6)
# print(children_sum_property(t.root))
print(max_width(t.root))