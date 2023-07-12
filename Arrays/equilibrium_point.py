def preprocess(l):
    a=l
    sum=0
    index=0
    for i in a:
        sum+=i
        a[index]=sum
        index+=1
    return a
def equilibrium_point(l):
    for i in range(1,len(l)-1):
        if l[len(l)-1]-l[i-1]==l[i]:
            print( l[i]-l[i-1])
            return
    else:
        print("There is no equilibrium point")

l=[3,4,8,-9,20,6]
a=preprocess(l)
print(a)
equilibrium_point(a)