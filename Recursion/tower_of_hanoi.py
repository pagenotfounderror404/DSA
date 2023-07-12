def tower0fhanoi(n,a,b,c,k=0):
    if n==1:
        print(f"Move 1 from {a} to {c}")
        return
    tower0fhanoi(n-1,a,c,b,k+1)
    print(f"Move {n} from {a} to {c}")
    tower0fhanoi(n-1,b,a,c,k+1)
    # print(f"Move {n} from b to c")


n=int(input("Enter n:"))
tower0fhanoi(n,'a','b','c')
