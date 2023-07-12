def bfs(l,s):
    dist=[float("inf") for i in range(len(l))]
    dist[s]=0
    visited=[False for i in range(len(l))]
    visited[s]=True
    queue=[]
    queue.append(s)
    while len(queue)!=0:
        u=queue.pop(0)
        for i in l[u]:
            if visited[i]==False:
                dist[i]=dist[u]+1
                queue.append(i)
                visited[i]=True
    print(dist)
l=[[1,2],[0,3],[0,3],[1,2]]
bfs(l,0)