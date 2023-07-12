from collections import deque


class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i
def binarytree_from_inorder_and_preorder(i,p,ist,ied):
    if ist>ied:
        return None
    node=Node(p[binarytree_from_inorder_and_preorder.pi])
    binarytree_from_inorder_and_preorder.pi+=1
    if ist==ied:
        return Node
    index=search(i,ist,ied,node.data)
    node.left=binarytree_from_inorder_and_preorder(i,p,ist,index-1)
    node.right=binarytree_from_inorder_and_preorder(i,p,index+1,ied)
    return node
binarytree_from_inorder_and_preorder.pi=0
def tree_traversal_spiral(root):
    q=deque()
    count=0
    q.append(root)
    while q:
        length=len(q)
        if count%2==0:
            for i in range(length):
                print(q[i].data, end=" ")
        else:
            for i in range(length-1,-1,-1):
                print(q[i].data, end=" ")
        count+=1
        while length!=0:
            length-=1
            temp=q.popleft()
            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)
t=Tree()
t.root=Node(8)
t.root.right=Node(2)
t.root.left=Node(6)
t.root.left.right=Node(7)
t.root.left.left=Node(9)
tree_traversal_spiral(t.root)
