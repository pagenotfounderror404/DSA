def oneton(n,s=1):
    if(s>n):
        return
    print(s)
    oneton(n,s+1)

n=int(input("Enter n: "))


def onetoonlyn(n):
    if (n==0):
        return
    onetoonlyn(n-1)
    print(n)

onetoonlyn(n)