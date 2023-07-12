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
    def reverse(self):
        self.queue.reverse()