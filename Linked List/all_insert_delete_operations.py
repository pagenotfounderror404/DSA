class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class Linked_list:
    def __init__(self):
        self.headval=None
    def print_linked_list(self):
        s=self.headval
        while s!=None:
            print(s.dataval,end=" ")
            s=s.next
        print("\n")
    def insert_in_begin(self,newnode):
        newnode.next=self.headval
        self.headval=newnode
        self.headval.dataval=newnode.dataval
    def insert_at_end(self,newnode):
        s=self.headval
        while s!=None:
            if s.next is None:
                s.next=newnode
                s.next.dataval=newnode.dataval
                newnode.next=None
            s = s.next
    def delete_first_node(self):
        s=self.headval
        self.headval=s.next
    def delete_last_node(self):
        s = self.headval
        while s != None:
            if s.next.next is None:
                s.next=None
                return
            s = s.next
    def insert_node_the_given_position(self,e,pos):
        s=self.headval
        for i in range(pos-2):
            s=s.next
            if s==None:
                self.print_linked_list()
                return
        e.next=s.next
        s.next=e
        s.next.dataval=e.dataval

e=Node(0)
p=Node(6)
l=Linked_list()
l.headval=Node(1)
l.headval.next=Node(2)
l.headval.next.next=Node(3)
e1=l.headval.next.next
e1.next=Node(4)
e1.next.next=Node(5)

l.insert_in_begin(e)
l.insert_at_end(p)
l.print_linked_list()
l.delete_first_node()
l.print_linked_list()
l.delete_last_node()
l.print_linked_list()
l.insert_node_the_given_position(e,8)
l.print_linked_list()