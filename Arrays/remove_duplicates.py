def remove_dupli(l):
    for i in l:
        for j in l[l.index(i)+1:]:
            if i==j:
                l.remove(i)
    return l
l=[10,10,20,20,20,30]

def remove_dupli1(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
        l=a
    return l


def remove_dupli3(l):
    s=0
    for i in l:
        if i not in l[l.index(i)+1:]:
            l[s]=i
            s+=1
        else:
            l.remove(i)

    return l
print(remove_dupli3(l))