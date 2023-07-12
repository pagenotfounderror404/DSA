class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def dequeue(self):
        self.head=self.head.next

    def enqueue(self,e):
        s = self.head
        while s.next== None:
            s = s.next
        s.next = e
    def get_front(self):
        s=self.head
        while s.next== None:
            s = s.next
        return s
    def get_rear(self):
        return self.head.data