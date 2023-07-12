def sliding_window(l,k):
    r=sum(l[0:k])
    for i in range(len(l)-k+1):
        if r<sum(l[i:i+k]):
            r=sum(l[i:i+k])
    return r
l=[1,8,30,-5,20,7]


def sliding_window1(l,k):
    r=0
    sum=0
    s=0
    for i in range(len(l)):
        if s<k:
            sum=sum+l[i]
            s+=1
        else:
            sum+=l[i]
            sum-=l[i-k]
            s+=1
            if sum>r:
                r=sum
    return r

def n_obnacci_number(n,limit):
    for i in range(n-1):
        print(0,end=",")
    print(1,end=",")
    s=1
    sub=1
    count=0
    for i in range(limit-3):
        if i==0:
             print(s,end="")
        else:
             print(",",s,end="")
        if i<n-1:
            s+=s
        else:
            if sub==1 and count==0:
                s+=s-sub
                sub=1
            else:
                s += s - sub
                sub += sub



n_obnacci_number(4,10)