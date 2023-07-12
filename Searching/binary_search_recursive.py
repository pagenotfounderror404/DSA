def binary_search_recursive(l,e,high,low=0):
    mid=int((high+low)/2)
    if high>low:
        if e==l[mid]:
            print(mid)
            return
        if e > l[mid]:
            binary_search_recursive(l,e,high,mid+1)
        if e<l[mid]:
            binary_search_recursive(l,e,mid-1,low)
    else:
        print(-1)
        return

l=[10,20,30,40,50,60,70]
e=20
high=len(l)
binary_search_recursive(l,e,high)