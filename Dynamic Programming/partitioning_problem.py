def ispalindrome(s,i,j):
    return s[i:j+1]==s[i:j+1:-1]
def palpart(st):
    n=st.length()
    dp=[[0 for i in range(n)] for i in range(n)]
    for gap in range(1,n):
        for i in range(0, n-gap):
            j=i+gap
            if ispalindrome(st,i,j):
                dp[i][j]=0
            else:
                dp[i][j]=float("inf")
                for k in range(i,j):
                    dp[i][j]=min(dp[i][j],1+dp[i][k]+dp[k+1][j])

    return dp[0][n-1]
