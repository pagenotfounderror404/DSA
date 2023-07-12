def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        for j in range(i):
            if l[i]<l[j]:
                del l[i]
                l.insert(j,key)
                break
    return l
# l=[57 ,38 ,91 ,10 ,38 ,28, 79 ,41]
# print(insertion_sort(l))

