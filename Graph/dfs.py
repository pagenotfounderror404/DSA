def dfsrec(d,s,visited):
    visited[s]=True
    print(s, end=" ")
    for i in d[s]:
        if visited[i]==False:
            dfsrec(d,i,visited)
def dfs(d,s):
    visited=[False for i in range(len(d)) ]
    dfsrec(d,s,visited)

d={}
d[0]=[1,4]
d[1]=[2]
d[2]=[1,3]
d[3]=[2]
d[4]=[5,6]
d[5]=[4,6]
d[6]=[4,5]
dfs(d,0)