class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
def search(root,key):
    if root==None:
        return False
    if root.data==key:
        return True
    if root.data>key:
        return search(root.left,key)
    if root.data<key:
        return search(root.right,key)
