def optimal_strategy(arr,i,j):
    if i+1==j:
        return max(arr[i+1],arr[j])
    return max (arr[i]+min(optimal_strategy(arr,i+1,j-1),optimal_strategy(arr,i+2,j)),arr[j]+min(optimal_strategy(arr,i,j-2),optimal_strategy(arr,i+1,j-1)))
def optimal_strategydp(arr):
    dp=[[0for i in range(len(arr))]for j in range(len(arr))]
    for i in range(len(arr)-1):
        dp[i][i+1]=max(arr[i],arr[i+1])
    for gap in range(len(arr),2):
        for i in range(len(arr)-gap):
            j=i+gap
            dp[i][j]=max(arr[i]+min(dp[i+1][j], dp[i+1][j-1]),arr[j]+min(dp[i][j-2],dp[i+1][j-1]))
    return dp[0][len(arr)-1]
