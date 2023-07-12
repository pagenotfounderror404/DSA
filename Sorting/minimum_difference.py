def minimum_difference(l):
    res=0
    l.sort()
    min=float('inf')
    for i in range(1,len(l)):
        if min>l[i]-l[i-1]:
            min=l[i]-l[i-1]
            res=l[i-1],l[i]
    print(min)

l=[10,3,20,12]
minimum_difference(l)