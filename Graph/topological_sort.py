def indegree(d):
        indegree = [0] * len(d)
        a = 0
        for i in d:
            for j in d[i]:
                indegree[j] += 1
        return indegree


def topological_sort(d):
    indeg=indegree(d)
    q=[]
    for i in range(len(indeg)):
        if indeg[i]==0:
            q.append(i)
    while len(q)!=0:
        u=q.pop(0)
        print(u,end=" ")
        for i in d[u]:
            indeg[i]-=1
            if indeg[i]==0:
                q.append(i)






d={}
d[0]=[2,3]
d[1]=[3,4]
d[2]=[3]
d[3]=[]
d[4]=[]
topological_sort(d)