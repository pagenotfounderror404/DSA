def naive_two_pivot_problem(l,p):
    ele=l[p]
    j=0
    for i in range(len(l)):
        if l[i]<ele:
            l[i],l[j]=l[j],l[i]
            j+=1
    for i in range(j+2,len(l)):
        if ele==l[i]:
            l.insert(j+1,l[i])
            del l[i+1]
            j+=1
    print(l)


def partition_around_a_range(l,low,high):
    j=0
    k=0
    for i in range(len(l)):
        if l[i]<low:
            l[j],l[i]=l[i],l[j]
            j+=1
            k+=1
        elif l[i]>=low and l[i]<=high:
            l[i],l[k]=l[k],l[i]
            k+=1
    print(l)



l=[10,5,6,3,20,9,40]
partition_around_a_range(l,5,10)