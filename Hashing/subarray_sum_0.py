def sum_subarray_0(a):
    d=[]
    d.append(a[0])
    for i in range(1,len(a)):
        d.append(d[i-1]+a[i])
    if set(d)!=d:
        print("yes")
    else:
        print("no")

a=[1,4,13,-10,-3]
sum_subarray_0(a)