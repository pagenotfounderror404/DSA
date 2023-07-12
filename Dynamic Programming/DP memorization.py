def fib(n):
    if fib.m[n]==-1:
        if n==0 or n==1:
            res=n
        else:
            res=fib(n-1)+fib(n-2)
        fib.m[n]=res
    return fib.m[n]

n=int(input())
fib.m=[-1 for i in range(n+1)]
print(fib(n))