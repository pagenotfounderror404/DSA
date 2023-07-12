def frequency_in_sorted_array(l):
    f=1
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            f+=1
        if l[i]!=l[i+1]:
            print(l[i],f)
            f=1
        if i+1==len(l)-1:
            print(l[i+1], f)
l=[10,10,10,25,30,30]
frequency_in_sorted_array(l)