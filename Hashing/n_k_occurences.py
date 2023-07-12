def n_k_occurences(a,k):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    s=int(len(a)/k)
    for i in d:
        if d[i]>s:
            print(i, end=" ")
arr=[30,10,20,20,10,20,30,30]
n_k_occurences(arr,4)