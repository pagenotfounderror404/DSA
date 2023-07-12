def ed(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m]==s2[n]:
        return ed(s1,s2,m-1,n-1)
    else:
        return 1+min(ed(s1,s2,m-1,n),ed(s1,s2,m,n-1),ed(s1,s2,m-1,n-1))
def ed_dp(s1,s2):
    dp=[[0 for i in range(len(s1)+1)]for i in range(len(s2)+1)]
    s=0
    for i in range(len(s1)+1):
        dp[i][0]=s
        s+=1
    s=0
    for i in range(len(s2)+1):
        dp[0][i] = s
        s += 1
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            dp[i][j]=dp[i-1][j-1]
            if s1[i]!=s2[j-1]:
                dp[i][j]=1+min(dp[i][j],dp[i-1][j],dp[i][j-1])
    return dp[len(s1)][len(s2)]