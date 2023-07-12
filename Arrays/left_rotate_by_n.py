def left_rotate_by_1(l,d):
    s=l[:d]
    for i in s:
        l.remove(i)
        l.append(i)
    return l
l=[1,2,3,4,5,1,4,1,7]
n=5
print(left_rotate_by_1(l,n))
