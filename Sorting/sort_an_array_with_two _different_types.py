def sort_on_the_basis_of_types(l):
    j=0
    i=0
    while i+j<=len(l):
        if l[i]<0:
            l[j],l[i]=l[i],l[j]
            j+=1
        else:
            i+=1
    print(l)
l=[15,-3,-2,18]
sort_on_the_basis_of_types(l)