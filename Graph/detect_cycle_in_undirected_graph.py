def dfsrec(d,s,visited,parent):
    visited[s]=True
    for i in d[s]:
        if visited[i]==False:
            if dfsrec(d,i,visited,s):
                return True
        elif i!=parent:
            return True
    return False
def dfs(d,s):
    visited=[False for i in range(len(d))]
    return dfsrec(d,s,visited,-1)
