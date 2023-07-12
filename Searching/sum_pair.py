#Two Pointer Approach
def sum_pair_search(l,s):
    high=len(l)-1
    low=0
    while(high>low):
        if l[high]+l[low]==s:
            return low,high
        if l[high] + l[low] > s:
            high-=1
        if l[high] + l[low] < s:
            low+=1
    return -1

l=[2,5,8,12,30]
print(sum_pair_search(l,18))