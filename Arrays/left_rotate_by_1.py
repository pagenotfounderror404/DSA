def left_rotate_by_1(l):
    s=l[0]
    l.remove(l[0])
    l.append(s)
    return l
l=[1,2,3,4,5,1,4,1,7]
print(left_rotate_by_1(l))
