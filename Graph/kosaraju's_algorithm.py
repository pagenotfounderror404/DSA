def dfsrec(d,u,st,visited):
    visited[u]=True
    for i in d:
        if not visited[i]:
            dfsrec(d,i,st,visited)
    st.append(u)

def dfsre(d,s,visited):
    visited[s]=True
    print(s, end=" ")
    for i in d[s]:
        if visited[i]==False:
            dfsre(d,i,visited)

def kosaraju_algo(d):
    st=[]
    visited=[False]*len(d)
    visited1=[False]*len(d)
    for i in d:
        if not visited[i]:
            dfsrec(d,i,st,visited)
    while len(st)!=0:
        res=st.pop(-1)
        dfsre(d, res, visited1)
        print()
