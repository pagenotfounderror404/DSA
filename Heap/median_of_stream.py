def median_of_stream(arr):
    temp=[]
    for i in  range(len(arr)):
        for j in range(len(temp)):
            if arr[i]<temp[j]:
                temp.insert(j,arr[i])
                break
        else:
            temp.append(arr[i])
        print(median(temp),end=" ")
def median(temp):
    size=len(temp)
    if size%2!=0:
        return float(temp[size//2])
    else:
        return float((temp[size//2]+temp[(size-1)//2])/2)
arr=[25,7,10,15,20]
median_of_stream(arr)