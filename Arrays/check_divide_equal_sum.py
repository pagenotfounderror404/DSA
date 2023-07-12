def preprocess(l):
    a=l
    sum=0
    index=0
    for i in a:
        sum+=i
        a[index]=sum
        index+=1
    return a
def check_divide(l):
    s=0
    if l[-1]%3==0:
        for i in l:
            if i ==  l[-1] / 3:
                s+=1
            if i==(2*l[-1])/3:
                s+=1
    if s==2:
        print("True")
    else:
        print("False")

l=[5,2,6,1,1,1,5]
a=preprocess(l)
check_divide(a)