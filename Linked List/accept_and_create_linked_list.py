class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None


def create_linked_list():
    global node
    n=int(input())
    l=LinkedList()
    for i in range(n):
        p=input()
        if i==0:
            l.head=Node(p)
            node=l.head
        else:
            node.next=Node(p)
            node=node.next
    return l.head

def print_linked_list(l):
    while l is not None:
        print(l.data, end=" ")
        l=l.next
l=create_linked_list()
print_linked_list(l)
