def fib(n):
    l=[]
    l.append(0)
    l.append(1)
    for i in range(2,n):
        l.append(l[i-2]+l[i-1])
    return l[n-1]
print(fib(5))