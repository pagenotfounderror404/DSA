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

def balanced_brackets(s):
    stack=Stack(len(s))
    for i in s:
        if i=="(" or i=="{" or i=="[":
            stack.push(i)
        elif i==")":
            e=stack.peek()
            if e=="(":
                stack.pop()
            else:
                print("Unbalanced")
                return
        elif i=="]":
            e=stack.peek()
            if e=="[":
                stack.pop()
            else:
                print("Unbalanced")
                return
        elif i=="}":
            e=stack.peek()
            if e=="{":
                stack.pop()
            else:
                print("Unbalanced")
                return

    e=stack.display()
    if len(e)==0:
        print("Balanced")
    else:
        print("Not Balanaced")



s="[]{(8+9858})}"
balanced_brackets(s)