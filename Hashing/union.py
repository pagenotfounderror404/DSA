def union(a,b):
    d={}
    s=0
    for i in a:
        if i not in d:
            d[i]=1
            s+=1

    for i in b:
        if i not in d:
            d[i]=1
            s+=1
    return s
a=[15,20,15,5]
b=[15,15,15,20,10]
print(union(a,b))