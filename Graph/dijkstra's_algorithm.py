def dijkistra_algo(d,s):
    v=len(d)
    dist=[float("inf")]*v
    fin=[False]*v
    dist[s]=0
    for count in range(v-1):
        u=-1
        for i in range(v):
            if not fin[i] and (u==-1 or dist[i]<dist[u]):
                u=i
        fin[u]=True
        for i in range(v):
            if not fin[i] and d[u][i]!=0:
                dist[i]=min(dist[i],dist[u]+d[u][i])
    return dist

