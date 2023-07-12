def cycle_sort_distinct(l):
    for cs in range(len(l)):
        item=l[cs]
        pos=cs
        for i in range(cs+1,len(l)):
            if l[i]<item:
                pos+=1
        l[pos],item=item,l[pos]
        while pos!=cs:
            pos=cs
            for i in range(cs+1,len(l)):
                if l[i] < item:
                    pos+=1
            l[pos], item = item, l[pos]
l=[20,40,50,10,30]
cycle_sort_distinct(l)
print(l)