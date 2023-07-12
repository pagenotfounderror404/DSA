def count_bst(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    for i in range(1,len(dp)):
        for j in range(i):
            dp[i]+=dp[j]*dp[i-j-1]
    return dp[n]
print(count_bst(5))