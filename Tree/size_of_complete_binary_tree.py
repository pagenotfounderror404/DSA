class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
def count_node(root):
    lh=0
    rh=0
    cur=root
    while cur!= None:
        cur=cur.left
        lh+=1
    cur=root
    while cur != None:
        cur = cur.right
        rh += 1
    if lh==rh:
        return pow(2,lh)-1
    return 1+count_node(root.left)+count_node(root.right)
