def binary_search_first_occurence(a,e):
    low=0
    high=len(a)-1
    while(high>low):
        mid = int((low + high) / 2)
        if e<a[mid]:
            high=mid-1
        if e>a[mid]:
            low=mid+1
        if e==a[mid]:
            if e!=a[mid-1]:
                # print(mid)
                return mid
            else:
                high-=1

            # for i in range(mid+1):
            #     if a[mid-1]==e:
            #         mid-=1
            #     else:
            #         print(mid)
            #         return

    # print(-1)
    return -1
x=20
l=[5,10,15,20,20,20]
binary_search_first_occurence(l,x)