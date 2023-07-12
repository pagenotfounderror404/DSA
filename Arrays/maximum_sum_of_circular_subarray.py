def max_sum_cirular_subarray(l):
    maxending1=l[0]
    maxending2=l[1]
    for i in range(1,len(l)):
        maxending1=max(maxending1+l[i],l[i])
    l.append(l[0])
    l.pop(0)
    for i in range (1,len(l)):
        maxending2 = max(maxending2 + l[i], l[i])
    maxending=max(maxending2,maxending1)
    return maxending

l=[-5,-3]
print(max_sum_cirular_subarray(l))