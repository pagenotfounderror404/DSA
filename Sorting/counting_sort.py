def counting_sort_for_integers(l,k):
    count=[0 for i in range(k)]
    # for i in range (k):
    #     sum = 0
    #     for j in l:
    #         if i ==j:
    #             sum+=1
    #     count.append(sum)
    for i in l:
        count[i]+=1
    l=[]
    for i in range(len(count)):
        for j in range(count[i]):
            l.append(i)


def counting_sort_for_objects(l,k):
    count=[0 for i in range(k)]
    output=[0 for i in range(len(l))]
    for i in l:
        count[i]+=1
    for i in range(1,k):
        count[i]+=count[i-1]
    for i in range(len(l)-1,-1,-1):
        output[count[l[i]]-1]=l[i]
        count[l[i]]-=1
    l=output
    print(l)


l=[1,4,4,1,0,1]
counting_sort_for_objects(l,6)



