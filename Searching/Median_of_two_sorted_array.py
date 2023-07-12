def median(a1,a2):
    n1=len(a1)-1
    n2=len(a2)-1
    begin1=0
    end1=n1

    while begin1<=end1:
        i1= int((begin1+end1)/2)
        i2=int((n1+n2+1)/2)-i1
        if i1==n1:
            min1=float('inf')
        else:
            min1=a1[i1]

        if i1==0:
            max1=-float('inf')
        else:
            max1=a[i1-1]
        if i2 == n2:
            min2 = float('inf')
        else:
            min2 = a1[i2]

        if i2 == 0:
            max2 = -float('inf')
        else:
            max2 = a[i2 - 1]
        if max1<=min2 and max2<=min1:
            if (n1+n2)%2==0:
                return float((max(max2,max1)+min(min2,min1))/2)
            else:
                return float(max(max1,max2))
        elif max1>max2:
            end1=i1-1
        else:
            begin1+=1

l=[10,20,30,40,50]
a=[5,10,25,35,45]
print(median(l,a))