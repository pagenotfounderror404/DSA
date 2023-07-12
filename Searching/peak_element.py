def peak_element(l):
    high=len(l)-1
    low=0
    while(high>=low):
        mid=int((high+low)/2)
        if (mid==0 or l[mid]>=l[mid-1]) and (mid==len(l)-1 or l[mid]>=l[mid+1]):
            return mid
        if mid>0 and l[mid-1]>=l[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
l=[5,20,40,30,20,50,60]

print(peak_element(l))