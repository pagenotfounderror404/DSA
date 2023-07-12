class Minheap:
    def __init__(self):
        self.arr=[]
    def left(self,i):
        return (2*i)+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def insert(self,x):
        self.arr.append(x)
        i=len(self.arr)-1
        while i!=0 and self.arr[self.parent(i)]>self.arr[i]:
            self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)
    def minheapify(self,i):
        lt=self.left(i)
        rt=self.right(i)
        smallest=i
        if self.arr[lt]<self.arr[i]:
            smallest=lt
        if self.arr[rt] < self.arr[i]:
            smallest = rt
        if smallest!=i:
            self.arr[i],self.arr[smallest]=self.arr[smallest],self.arr[i]
            self.minheapify(smallest)



