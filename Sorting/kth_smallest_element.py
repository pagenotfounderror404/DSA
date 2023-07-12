def kth_smallest_element(l,k):
    for i in range(k-1):
        p=min(l)
        l.remove(p)
    print(min(l))
a=[30,20,5,10,8]
kth_smallest_element(a,4)

