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
def stock_span(a):
    l=[1]
    s=Stack(len(a))
    s.push(0)
    for i in range(1,len(a)):
        while len(s.display())!=0 and a[s.peek()]<=a[i]:
            s.pop()
        if len(s.display())==0:
            l.append(i+1)
        else:
            l.append(i-s.peek())
        s.push(i)



    print(l)
l=[13,15,12,14,16,8,6,4,10,30]
stock_span(l)

