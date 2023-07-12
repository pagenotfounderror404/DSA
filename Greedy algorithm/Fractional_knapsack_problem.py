def fractional_knapsack_problem(l,k):
    a=[]
    d={}
    for i in l:
        d[int(i[1]/i[0])]=i
        a.append(int(i[1]/i[0]))
    a.sort()
    a.reverse()
    res=0
    i = 0
    while k>0:
        if k>=d[a[i]][0]:
            k-=d[a[i]][0]
            res+=d[a[i]][1]
        else:
            res+=k*d[a[i]][1]/d[a[i]][0]
            return res
        i+=1
    return res
a=[[50,600],[20,500],[30,400]]
k=70
print(fractional_knapsack_problem(a,k))