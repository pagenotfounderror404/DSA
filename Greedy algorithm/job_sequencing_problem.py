def job_sequencing_problem(j,p):
    d={}
    for i in range(len(p)):
        d[p[i]]=j[i]
    p.sort()
    p.reverse()
    k=[0 for i in range(max(j))]
    for i in range(len(p)):
        if k[d[p[i]]-1]==0:
            k[d[p[i]]-1]=p[i]
        else:
            for i in range(d[p[i]]-1,-1,-1):
                if k[i]==0:
                    k[i]=p[i]
                    break
    print(k,sum(k))


j=[4,1,1,5,5]
p=[50,5,20,10,80]
job_sequencing_problem(j,p)


