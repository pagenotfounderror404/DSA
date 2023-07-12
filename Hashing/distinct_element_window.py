def  distinct_element_window(a,k):
    for i in range(0,len(a)):
        if i+k<=len(a):
            print(len(set(a[i:i+k])), end=" ")
a=[10,20,20,10,30,40,10]
distinct_element_window(a,4)

