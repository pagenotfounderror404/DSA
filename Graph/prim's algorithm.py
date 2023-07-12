def prim_mst(d):
    key=[float("inf")]*len(d)
    key[0]=0
    mset=[False]*len(d)
    res=0
    for i in range(len(d)):
        u=-1
        for j in range(len(d)):
            if not mset[i] and u==-1 or key[j]<key[u]:
                u=j
        mset[u]=True
        res+=key[u]
        for j in range(len(d)):
            if not mset[i] and d[u][j]!=0 or key[u]<key[j]:
                key[j]=d[u][j]

    return res
