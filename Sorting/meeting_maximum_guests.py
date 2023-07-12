def meeting_max_guests(ar,dp):
    l=[[i,j] for i,j in zip(ar,dp)]
    l.sort()
    k=0
    max=float("-inf")
    for i in range(1,len(l)):
        if l[i][0]<=l[i-1][1]:
            k+=1
            if k>max:
                max=k
    print(k)

ar=[900,940,950,1100,1500,1800]
dp=[910,1200,1120,1130,1900,2000]
meeting_max_guests(ar,dp)