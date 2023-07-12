def longest_subarray_with_given_sum(a,s):
    d={}
    k=[]
    sum=0
    for i in range(len(a)):
        sum += a[i]
        k.append(sum)
        if sum not in d:
            d[sum]=[i]
        else:
            d[sum].append(i)
    max_idx=0
    for i in range(len(a)-1,-1,-1):
        if k[i]-s in d:
            max_idx=max(max_idx, i-min(d[k[i]-s])+1)
        else:
            if len(d[k[i]])==1:
                del d[k[i]]
            else:
                d[k[i]].remove(i)

    print(max_idx)
a=[8,3,1,5,-6,6,2,2]
longest_subarray_with_given_sum(a,4)