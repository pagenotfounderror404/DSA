class Stack:
    def __init__(self,maxsize):
        self.stack=[]
        self.size=maxsize
    def push(self,a):
        if len(self.stack)>=self.size:
            print("Overflow")
            return
        self.stack.append(a)
    def pop(self):
        if len(self.stack)==0:
            print("Underflow")
            return
        del self.stack[-1]
    def peek(self):
        try:
            print(self.stack[-1])
        except IndexError:
            print("Not found")

    def display(self):
        print(self.stack)

s=Stack(4)
s.push(5)
s.peek()
s.pop()
s.peek()
s.push(5)
s.push(2)
s.push(3)
s.peek()
s.display()
s.pop()
s.display()
s.push(6)
s.push(8)
s.push(9)
s.display()