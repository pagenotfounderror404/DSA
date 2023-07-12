def k_closest_element(arr,x,k):
    global index
    arr.sort()
    if x in arr:
        index=arr.index(x)
    else:
        for i in range(1,len(arr)):
            if arr[i-1]<x and arr[i]>x:
                index=i
    for i in range(index-(k//2),index+(k//2)+1):
        print(arr[i])
