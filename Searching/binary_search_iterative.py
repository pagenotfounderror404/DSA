def binary_search(a,e):
    low=0
    high=len(a)-1
    while(high>low):
        mid = int(low + high / 2)
        if e<a[mid]:
            high=mid-1
        if e>a[mid]:
            low=mid+1
        if e==a[mid]:
            return mid+1
    return -1
l=[10,10]
e=5
binary_search(l,e)