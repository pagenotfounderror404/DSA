def lis(a):
    dp=[1 for i in range(len(a))]
    a_sort=sorted(a)
    s=0
    for i in range(1,len(a)):
        if a[i] in a_sort[a_sort.index(a[0]):]:
            while a_sort[a_sort.index(a[i])-s] not in a[:i] and a_sort.index(a[i])-s!=0:
                s+=1
            dp[i]=1+dp[a.index(a_sort[a_sort.index(a[i])-s])]
        s=0
    print(max(dp))
def lis2(a):
    dp = [1 for i in range(len(a))]
    p=[]
    p.append(a[0])
    for i in range(1,len(a)):
        for j in range(len(p)):
            if a[i]<=p[j]:
                p.insert(j,a[i])
                index = p.index(a[0])
                if a[i] in p[index:]:
                    dp[i] = 1 + dp[a.index(p[j-1])]
                break
        else:
            p.append(a[i])
            index = p.index(a[0])
            if a[i] in p[index:]:
                dp[i] = 1 + dp[a.index(p[len(p) - 2])]
    print(max(dp))
a=[3,4,2,8,10,5,1]
lis2(a)