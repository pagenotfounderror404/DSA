def naive_partition(l,p):
    if p<len(l):
        k=[]
        k.append(l[p])
        index=0
        l.remove(l[p])
        for i in l:
            if i<=k[index]:
                k.insert(index,i)
                index+=1
            else:
                k.append(i)
        print(k)



def swap_partition(l,p):
    if p<len(l):
        index = p
        s=l[p]
        for i in range(len(l)):
            if l[i]>l[index] and index>i:
                l[i],l[index]=l[index],l[i]
                index=l.index(s)
            elif l[i] <= l[index] and index < i:
                l.insert(index,l[i])
                del l[i+1]
                index=l.index(s)
    print(l)



def loumo_partition(l,low,high):
    pivot=l[high]
    i=low-1
    for j in range(low,high):
        if l[j]<pivot:
            i+=1
            l[i], l[j] = l[j], l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return i+1

def hoare_partition(l,low,high):
    pivot=l[low]
    i=low
    j=high
    while j>=i and j!=0:
        if l[i]<pivot:
            i+=1
        elif l[j]>pivot:
            j-=1
        elif l[i]>=pivot and l[j]<pivot:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1



def hoare_partition2(a, low, high):
    pivot = a[low]
    (i, j) = (low - 1, high + 1)

    while True:

        while True:
            i = i + 1
            if a[i] >= pivot:
                break

        while True:
            j = j - 1
            if a[j] <= pivot:
                break

        if i >= j:
            return j

        a[i],a[j]=a[j],a[i]




l=[5,3,8,4,7,1,10]
