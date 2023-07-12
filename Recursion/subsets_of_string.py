def subset(n,k=0,curr=""):
    if k==len(n):
        print(curr)
        return n

    subset((n),k+1,curr)
    subset(n,k+1, curr+n[k])


n="abc"
print(str(subset(n)))