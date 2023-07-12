def activity_selection_problem(a):
    r=[]
    a.sort()
    r.append(a[0])
    for i in range(1,len(a)):

        if  a[i][0]>=r[len(r)-1][1]:
            r.append(a[i])
    print(r)



a=[[3,8],[2,4],[1,3],[10,11]]
activity_selection_problem(a)