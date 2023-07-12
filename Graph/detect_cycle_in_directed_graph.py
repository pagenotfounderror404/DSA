def dfsrec(a,s,visited,recst):
    visited[s]=True
    recst[s]=True
    for i in a[s]:
        if visited[i]==False and dfsrec(a,i,visited,recst):
            return True
        elif recst[i]==True:
            return True
    recst[s]=False
    return False
def dfs(a):
    visited=[False]* len(a)
    recst=[False]* len(a)
    for i in range(len(a)):
        if visited[i]==False:
            if dfsrec(a,i,visited,recst):
                return True
    return False
