def count_distinct_element(d,k):
    if k in d:
        d[k]+=1
    else:
        d[k]=1
k=[15,12,13,12,13,13,18]
d={}
for i in k:
    count_distinct_element(d,i)
print(len(d))
for i in d:
    print(i,d[i])