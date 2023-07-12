def countways(coins,n,s):
    if s==0:
        return 1
    if s<0:
        return 0
    if n==0:
        return 0
    return countways(coins,n,s-coins[n-1])+ countways(coins,n-1,s)
def countways_dp(coins,n,s):
    w=[[0]*(s+1)]*(n+1)
    w[0][0]=1
    for i in range(1,n+1):
        for j in range(1,s+1):
            w[i][j]=w[i-1][j]
            if coins[i-1]<=j:
                w[i][j]+=w[i][j-coins[i-1]]
    return w[n][s]

# r=countways_dp([1,2,3],3,4)
# print(r)

r=[[0]*5]*2
r[0][0]=1
print(r)