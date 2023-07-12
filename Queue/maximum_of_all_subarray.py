def max_all_sub_array(l,k):
    max_sub=[]
    for i in range(len(l)-k+1):
        max_sub.append(max(l[i:i+k]))
    print(max_sub)
l=[10,8,5,12,15,7,6]
max_all_sub_array(l,3)