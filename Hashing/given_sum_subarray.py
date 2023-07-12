def given_sum_subarray(a,s):
    d=[]
    d.append(a[0])
    for i in range(1,len(a)):
        d.append(d[i-1]+a[i])
    for i in range(len(d)-1,-1,-1):
         if d[i]-s in d[:i-1]:
            print("yes")
            return
    print("no")

a=[5,8,6,13,3,-1]
given_sum_subarray(a,22)