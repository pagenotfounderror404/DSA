def majority_element(l):
    a={}
    maxele=0
    maxfreq=0
    for i in l:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    for i in a:
        if a[i]>maxfreq:
            maxele=i
            maxfreq=a[i]
    if maxfreq>len(l)/2:
        for i in range(len(l)):
            if l[i]==maxele:
                print(i)
    else:
        print(-1)


def moores_voting_algorthim(l):
    res=0
    cur=1
    for i in range(1,len(l)):
        if l[res]==l[i]:
            cur+=1
        else:
            cur-=1
        if cur==0:
            res=i
            cur=1
    count=0
    for i in l:
        if l[res]==i:
            count+=1
    if count>len(l)/2:
        print(res)
    else:
        print(-1)
    return

l=[1,2,6,6,1]
moores_voting_algorthim(l)

