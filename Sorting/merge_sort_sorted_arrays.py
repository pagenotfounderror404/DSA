def merge_sort_sorted_array(l,a):
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
a=[10,15,20,20]
l=[1,12]
print(merge_sort_sorted_array(l,a))