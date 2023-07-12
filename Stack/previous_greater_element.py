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
            return -1

    def display(self):
        return self.stack
def prev_greater(a):
    l=[-1]
    stack=Stack(len(a))
    stack.push(a[0])
    for i in range(1,len(a)):
        while stack.peek()<=a[i] or stack.peek()!=-1:
            stack.pop()
        if len(stack.display())==0:
            l.append(-1)
        else:
            l.append(stack.peek())
        stack.push(a[i])
    print(l)
l=[20,30,10,5,40]
prev_greater(l)

