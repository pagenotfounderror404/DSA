def check_sort(l):
    for i in l:
        for j in l[l.index(i):]:
            if i>j:
                print(i)
                return "not sorted"
    return "sorted"


def check_sort1(l):
    min=l[0]
    for i in l:
        if i<min:
            return "not sorted"
        else:
            min=i
    return "sorted"
l=[10,10,20,40,50]
print(check_sort1(l))

