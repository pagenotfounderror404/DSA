global memo
def lcs(s1,s2,m,n):
    if memo[m][n]!=-1:
        return memo[m][n]
    if m==0 or n==0:
        memo[m][n]=0
    else:
        if s1[m-1]==s2[n-1]:
            memo[m][n]=1+lcs(s1,s2,m-1,n-1)
        else:
            memo[m][n]=max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
    return memo[m][n]

def lcs2(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1)]*(m+1)
    for i in range(m+1):
        dp[i][0]=0
    for j in range(n+1):
        dp[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


s1="axyz"
s2="baz"
m=len(s1)
n=len(s2)
memo=[[-1]*(n)]*m
print(lcs(s1,s2,m-1,n-1))
print(lcs2(s1,s2))