def sum_subarray_0(a):
    d=[]
    k={}
    d.append(a[0])
    for i in range(1,len(a)):
        d.append(d[i-1]+a[i])
    for i in range(len(d)):
        if d[i] not in k:
            k[d[i]]=[i]
        else:
            k[d[i]].append(i)
    max_idx=0
    for i in k:
        if len(k[i])>1:
           max_idx=max(max_idx,max(k[i])-min(k[i]))
    print(max_idx)
def longest_subarray_with_equal_0_and_1(a):
    for i in range(len(a)):
        if a[i]==0:
            a[i]=-1
    sum_subarray_0(a)
a=[1,0,1,1,1,0,0]
longest_subarray_with_equal_0_and_1(a)
