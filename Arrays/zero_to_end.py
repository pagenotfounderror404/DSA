def zero_to_end(l):
    a=[]
    for i in l:
        if i==0:
            l.remove(i)
            l.append(i)
    return l

l=[1,0,2,3,0,4,0,2,0,0]
print(zero_to_end(l))