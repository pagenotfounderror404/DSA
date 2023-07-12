def reverse_arr(l):
    for i in range(int((len(l)+1)/2)):
        l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
    return l

l=[1,2,3,4]
print(reverse_arr(l))