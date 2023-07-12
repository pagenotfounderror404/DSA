def chocolate_distribution_problem(l,m):
    l.sort()
    res=0
    l.sort()
    print(l)
    min=float('inf')
    for i in range(m-1,len(l)):
        if min>l[i]-l[i-(m-1)]:
            min=l[i]-l[i-(m-1)]
            res=l[i-(m-1)],l[i]
    print(min)



l=[3,4,1,9,56,7,9,12]
chocolate_distribution_problem(l,5)