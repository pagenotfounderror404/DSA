def nto1(n):
    if(n==0):
        return
    print(n)
    nto1(n-1)

n=int(input("Enter n: "))

nto1(n)