class Stack:
    def __init__(self,maxsize):
        self.stack=[]
        self.size=maxsize
    def push(self,a):
        if len(self.stack)>=self.size:
            return "Overflow"
        self.stack.append(a)
    def pop(self):
        if len(self.stack)==0:
            return "Underflow"
        del self.stack[-1]
    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return "Empty"

    def display(self):
        return self.stack

a=[]
k=int(input())
for i in range(k):
    e=Stack(5)
    a.append(e)

