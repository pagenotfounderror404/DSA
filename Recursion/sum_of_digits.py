def sumdigits(n,k=0):
    if n<=0:
        return k
    return sumdigits(int(n/10),k+n%10)

n=int(input("Enter n: "))





def sumdigits1(n):
    if n<=0:
        return n
    return sumdigits(int(n/10))+n%10



print(sumdigits1(n))