def secondmax(l):
    max2=l[0]
    a=[]
    for i in l:
        if max2<i:
            max2=i
            a.append(l.index(max2))
    if a==[]:
        max2=l[1]
        for i in l:
            if max2 < i and i!=l[0]:
                max2 = i
                a.append(l.index(max2))
        if a==[]:
            return -1
        else:
            return a[-1]

    return a[-2]


def secondmax2(l):
    max=0
    res=-1
    for i in l:
        if max<i:
            res=max
            max=i
    if max==l[0]:
        for i in l:
            if res < i and i != l[0]:
                res= i
    return l.index(res)

l=[20,10,20,8,12]
print(secondmax2(l))

