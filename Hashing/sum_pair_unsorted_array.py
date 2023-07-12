def sum_pair(a,sum):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if sum-i==i and d[i]>1:
            print("yes")
            break
        elif sum-i in d and sum-i!=i:
            print("yes")
            break
    print("no")
a=[11,5,6]
sum=10
sum_pair(a,sum)