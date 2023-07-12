class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
def floor(root,key):
    if root==None:
        if floor.floor!=None:
            return floor.floor
        else:
            return None
    if root.data>key and root.left.data<key:
        floor.floor= root.left.data
    elif root.data<key and root.right.data>key:
        floor.floor= root.data
    elif root.data==key:
        floor.floor= root.data
    else:
        if root.data>key:
            floor(root.left,key)
        else:
            floor(root.right,key)
    return floor.floor
floor.floor=None