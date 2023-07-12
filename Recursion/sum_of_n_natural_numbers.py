def sumnatural(n,k):
    if n==0:
        return k
    return sumnatural(n-1,k+n)
n=int(input("Enter n: "))


def sumnatural1(n):
    if n<=1:
        return n

    return n+sumnatural1(n-1)


print(sumnatural1(n))

