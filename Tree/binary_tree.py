class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class Queue:
    def __init__(self):
        self.queue=[]
    def dequeue(self):
        e=self.queue[0]
        del self.queue[0]
        return e

    def bottom(self):
        return self.queue[0]
    def top(self):
        return self.queue[-1]
    def enqueue(self,e):
        self.queue.append(e)
    def lengthq(self):
        return len(self.queue)
class Tree:
    def __init__(self):
        self.root=None
    def inorder_traversal(self,root):
        if root!=None:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)
    def preorder_traversal(self,root):
        if root!=None:
            print(root.data, end=" ")
            self.inorder_traversal(root.left)
            self.inorder_traversal(root.right)
    def postorder_traversal(self,root):
        if root!=None:
            self.inorder_traversal(root.left)
            self.inorder_traversal(root.right)
            print(root.data, end=" ")
    def height(self,root):
        if root==None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
    def printdistance(self,root,k):
        if root==None:
            return
        if k==0:
            print(root.data, end=" ")
        else:
            self.printdistance(root.left,k-1)
            self.printdistance(root.right,k-1)
    def level_order_traversal(self,root):
        if root==None:
            return
        q=Queue()
        q.enqueue(root)
        while q.lengthq()!=0:
            cur=q.dequeue()
            print(cur.data, end=" ")
            if cur.left!=None:
                q.enqueue(cur.left)
            if cur.right!=None:
                q.enqueue(cur.right)


def printGivenLevel(root, level):
    if root is None:
        return root

    if level == 1:
        print(root.data, end=' ')
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def printlevelorder(l,root):
    h = l.height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()


t=Tree()
t.root=Node(8)
t.root.right=Node(1)
t.root.left=Node(6)
t.root.left.left=Node(9)
t.inorder_traversal(t.root)
print()
t.preorder_traversal(t.root)
print()
t.postorder_traversal(t.root)
print()
print(t.height(t.root))
t.printdistance(t.root,1)
print()
t.level_order_traversal(t.root)
print()
printlevelorder(t,t.root)