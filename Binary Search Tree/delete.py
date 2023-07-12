class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
def getsuccessor(root):
    curr=root.right
    while root!=None or root.left!=None:
        curr=curr.left
    return curr
def delete(root,x):
    if root==None:
        return None
    if root.data>x:
        root.left=delete(root.left,x)
    elif root.data<x:
        root.right=delete(root.right,x)

    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            succ= getsuccessor(root)
            root.data=succ.data
            root.right=delete(root.right,root.data)
    return root
