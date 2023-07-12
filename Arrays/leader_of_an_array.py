def maxelement(a,index):
    max=0
    for i in range(index,len(a)):
        if l[i]>max:
            max=l[i]

    return max

def leader_arr(l):
    a=[]
    for i in range (len(l)):
        if l[i]>maxelement(l,i+1):
            a.append(l[i])
    return a
l=[7,10,4,10,6,5,2]


def leaderarr1(l):
    max=0
    for i in range (len(l)-1,-1,-1):
        if l[i]>max:
            max=l[i]
            print(max,end=" ")

leaderarr1(l)
