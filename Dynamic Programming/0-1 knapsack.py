def knapsack0_1(wt,val):
    W=len(wt)
    n=len(val)
    dp=[[0 for i in range(W+1)] for j in range(n + 1)]
    for i in range(0,n+1):
        for j in range(0,W+1):
            if wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
        return dp[n][W]