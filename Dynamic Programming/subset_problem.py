def subset_problem(ar,sum):
    dp=[[0 for i in range(sum+1)]for i in range(len(ar)+1)]
    for i in range(len(ar)+1):
        dp[i][0]=1
    for i in range(1,len(ar)+1):
        for j in range(1,sum+1):
            if j<ar[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-ar[i-1]]
    return dp[len(ar)][sum]
print(subset_problem([2,5,3],5))