def maximum_difference(l): #exclude descending elements
    maxdiff=l[1]-l[0]
    for i in range(1,len(l)):
        if l[i]<max(l[i:]):
            if max(l[i:])-l[i]>maxdiff:
                print(max(l[i:])-l[i])
                maxdiff=max(l[i:])-l[i]
    print(maxdiff)

def maximum_difference1(l):
    minele=l[0]
    res=int(l[1]-l[0])
    for i in range(1,len(l)):
        res=max(res,l[i]-minele)
        minele=min(minele,l[i])
    return res

l=[2,3,10,6,4,8,1]
print(maximum_difference1(l))