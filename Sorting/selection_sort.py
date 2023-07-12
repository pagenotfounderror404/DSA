def selection_sort(l):
    for i in range(len(l)):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
        l[i],l[min]=l[min],l[i]
    return l
l=[20,50,10,40,60,80,10,40]
print(selection_sort(l))
