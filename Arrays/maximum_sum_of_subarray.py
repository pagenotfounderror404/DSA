def max_sum_subarray(l):
    res=l[0]
    for i in range(len(l)):
        for j in range(len(l)+1):
            if sum(l[i:j])>res and l[i:j]!=[]:
                res=sum(l[i:j])
    return res

def max_sum_subarray1(l):
    maxending=l[0]
    for i in range(len(l)):
        maxending=max(maxending+l[i],l[i])
    return maxending
l=[2,3,-8,7,-1,2,3]
print(max_sum_subarray(l))

