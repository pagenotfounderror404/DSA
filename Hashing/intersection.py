def intersection(a,b):
    d={}
    for i in a:
        d[i]=1
    s = 0
    for i in b:
        if i in d and d[i]<2:
            s+=1
            d[i]+=1
    return s
a=[10,15,20,15,30,30,5]
b=[30,5,30,80]
print(intersection(a,b))