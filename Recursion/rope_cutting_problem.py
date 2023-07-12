def ropecut(n,a,b,c):

    if n==0:
        return 0
    if n<0:
        return -1
    x=ropecut(n-a,a,b,c)
    y=ropecut(n-b,a,b,c)
    z=ropecut(n-c,a,b,c)
    r=max(x,y,z)
    if r<0:
        return -1
    return r+1
n=int(input("Enter n: "))
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

print(ropecut(n,a,b,c))