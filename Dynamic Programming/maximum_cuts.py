
def max_cuts(n,a,b,c):
    k=0
    while n>0:
        if  n%a==0:
            k+=(n/a)
            n=0
        if n % b == 0:
            k += (n / b)
            n = 0
        if  n % c == 0:
            k += (n / c)
            n = 0
        else:
            n-=min(a,b,c)
            k+=1
    if n==0:
        print(k)
    else:
        print(-1)

def max_cuts2(n,a,b,c):
    dp=[-1 for i in range(n+1)]

    dp[0] = 0

    for i in range(1,n+1):
        if i - a >= 0 :
            dp[i] = max(dp[i], dp[i-a])

        if i-b >= 0:
            dp[i] = max(dp[i], dp[i-b])
        if i-c >= 0 :
            dp[i] =max(dp[i], dp[i-c])

        if dp[i] != -1:
            dp[i]+=1

    return dp[n]

print(max_cuts2(24,11,12,13))
