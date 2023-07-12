class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
def serialize(root):
    if root!=None:
        serialize.l.append(root.data)
    else:
        serialize.l.append(-1)
        return
    serialize(root.left)
    serialize(root.right)
def desearialize(l):
    if desearialize.index==len(l):
        return None
    val=l[desearialize.index]
    desearialize.index+=1
    if val==-1:
        return None
    root=Node(val)
    root.left=desearialize(l)
    root.right=desearialize(l)
    return root
desearialize.index=0
serialize.l=[]
t=Tree()
t.root=Node(8)
t.root.right=Node(1)
t.root.left=Node(6)
t.root.left.left=Node(9)
serialize(t.root)
print(serialize.l)