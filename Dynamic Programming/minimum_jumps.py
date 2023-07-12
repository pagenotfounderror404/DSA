def minimum_jumps(a):
    dp=[float("inf") for i in range(len(a))]
    dp[0]=0
    for i in range(1,len(a)):
        for j in range(0, i):
            if a[j]+j>=i and dp[j]!=float("inf"):
                dp[i]=min(dp[i],dp[j]+1)
                break
    print(dp)
    return dp[-1]

a=[3,4,2,1,2,1]
minimum_jumps(a)
