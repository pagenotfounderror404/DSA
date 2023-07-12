def intersection(l,a):
    s=0
    p=0
    r=max(len(l),len(a))
    k=0
    i=0
    while(i<=r):
        i+=1
        if p>=len(a):
            p=len(a)-1
        if s>=len(l):
            s=len(l)-1
        if l[s]>a[p]:
            p+=1
        elif l[s]<a[p]:
            s+=1
        elif l[s]==a[p]:
            if k!=l[s]:
                print(l[s],end=" ")
            k = l[s]
            s+=1
            p+=1


l=[3,5,10,10,15,15,20]
a=[5,10,10,15,30]
intersection(l,a)