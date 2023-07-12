def fact(n):
    if(n==1):
        return n
    return int(n*int(fact(n-1)))

def facttail(n,k=1):
    if n<=1:
        return k
    return facttail(n-1,n*k)

n=int(input("Enter n: "))
print(fact(n))
print(facttail(n))