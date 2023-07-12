class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,e):
        e.next = self.head
        self.head = e
    def pop(self):
        if self.head!=None:
            self.head=self.head.next
        else:
            print("Underflow")
            return
    def peek(self):
        if self.head!=None:
            print(self.head.data)
            return
        else:
            print("Empty stach")
            return
    def size(self):
        count=0
        s=self.head
        while s!=None:
            count+=1
            s=s.next
        print(count)
