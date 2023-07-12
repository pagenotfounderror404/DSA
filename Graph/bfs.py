def bfs(l,s):
    bfs.visited[s]=True
    queue=[]
    queue.append(s)
    while len(queue)!=0:
        u=queue.pop(0)
        print(u, end=" ")
        for i in l[u]:
            if bfs.visited[i]==False:
                queue.append(i)
                bfs.visited[i]=True
    if False in bfs.visited:
        index=bfs.visited.index(False)
        bfs(l,index)


l=[[1,2],[0,3],[0,3],[1,2],[5,6],[4,6],[4,5]]
bfs.visited=[False for i in range(len(l))]
bfs(l,0)


