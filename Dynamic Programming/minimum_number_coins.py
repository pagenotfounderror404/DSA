def mincoin(a,l):
    if a==0:
        return 0
    res=float("-inf")
    for i in range(len(l)):
        if l[i]<=a:
            sub= mincoin(a-l[i],l)
            if sub!=float("-inf"):
                res=min(res,sub+1)
    return res
def mincoin2(coin,val):
    dp=[float("inf") for i in range(val+1)]
    dp[0]=0
    for i in range(1,val+1):
        for c in coin:
            if c-i<=0:
                dp[i]=min(dp[i],dp[i-c])
        if dp[i]!=float("-inf"):
            dp[i]+=1
    print(dp)
    return dp[val]


print(mincoin2([9,5,6,1],11))



