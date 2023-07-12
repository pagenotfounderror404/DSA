def merge_function_insertion_technique(l,b):
    for i in range(b,len(l)):
        s=l[b]
        for j in range(i):
            if s<l[0]:
                l.remove(s)
                l.insert(0, s)
            elif l[j]<=s and s<l[j+1]:
                l.remove(s)
                l.insert(j,s)
    return l

def merge_function_sorted_array_technique(l,b):
    a=l[b:len(l)]
    l=l[:b]
    s=0
    p=0
    k=len(l)+len(a)
    r=[]
    for i in range(k):
        if s==len(l):
            for j in range(p,len(a)):
                r.append(a[j])
            return r
        if p==len(a):
            for j in range(s,len(l)):
                r.append(l[j])
            return r
        if l[s]>a[p]:
            r.append(a[p])
            p+=1
        elif l[s] <a[p]:
            r.append(l[s])
            s += 1
        elif l[s]==a[p]:
            r.append(l[s])
            r.append(a[p])
            s+=1
            p+=1
    return r
l=[10,15,20,11,30]
print(merge_function_sorted_array_technique(l,3))
