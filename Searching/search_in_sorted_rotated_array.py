from binary_search_iterative import binary_search
from linear_search import linear_search
def sorted_in_rotated_array_search(l,e):
    high=len(l)-1
    low=0
    mid=int((low+high)/2)
    if l[mid]>l[low] and l[low]<=e and l[mid]>=e:
        binary_search(l[low:mid+1],e)
        return
    else:
        linear_search(l[mid+1:high+1],e)
    if l[mid]<l[high] and l[high]>=e and l[mid]<=e:
        binary_search(l[mid:high+1],e)
        return
    else:
        linear_search(l[low:mid-1],e)


def sorted_in_rotated_array_search_more_efficient(l,e):
    high=len(l)-1
    low=0
    while(high>low):
        mid=int ((high+low)/2)
        if l[mid]>l[low]:
            if e>=l[low] and e<l[mid]:
                high=mid-1
            else:
                low=mid+1
        if l[mid]<l[high]:
            if e<=l[high] and e>mid:
                low=mid+1
            else:
                high=mid-1
        if l[mid]==e:
            return mid
    return -1







l=[100,500,10,20,30,40,50]
e=500
print(sorted_in_rotated_array_search_more_efficient(l,e))
