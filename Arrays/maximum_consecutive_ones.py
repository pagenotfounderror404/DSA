def max_1(l):
    count =0
    a = []
    for i in range(1,len(l)):
        if l[i]==1 and l[i-1]==1:
            if count==0:
                count+=2
            else:
                count+=1
        else:
            a.append(count)
            count = 0
        if i==len(l)-1:
            a.append(count)
    return max(a)

l=[1,0,1,1,1,0,1,1,1,1]
print(max_1(l))