def max_appear(l,u):
    a=[]
    t=max(u)
    s=0
    b=0
    for i in range(t+2):
        if s<len(l):
            if i==l[s]:
                a.append(1)
                s+=1
            else:
                a.append(0)
        else:
            a.append(0)
    s=0
    for i in range(t+2):
        if s<len(u):
            a[u[s]+1]-=1
            s+=1

    return a
def preprocess(l):
    a=l
    sum=0
    index=0
    for i in a:
        sum+=i
        a[index]=sum
        index+=1
    return a

l=[1,2,3]
u=[5,3,7]
r=preprocess(max_appear(l,u))
print(r.index(max(r)))