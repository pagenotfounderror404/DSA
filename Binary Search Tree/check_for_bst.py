class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
def check_for_bst(root,min=float("-inf"),max=float("inf")):
    if root==None:
        return True
    return root.data>min and root.data<max and check_for_bst(root.left,min,root.data) and check_for_bst(root.right, root.data,max)
