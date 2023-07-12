class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
def insert(root,key):
    if root==None:
        node=Node(key)
        return node
    else:
        if root.data==key:
            return root
        elif root.data>key:
             root.left=insert(root.left,key)
        elif root.data<key:
            root.right=insert(root.right,key)
