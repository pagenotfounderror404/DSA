def max_sum_no_conse(ar):
    dp=[0 for i in range(len(ar)+1)]
    dp[1]=ar[0]
    for i in range(2,len(ar)+1):
        dp[i]=max(dp[i-1],dp[i-2]+ar[i-1])
    return dp[len(ar)]
print(max_sum_no_conse([10,5,15,20]))