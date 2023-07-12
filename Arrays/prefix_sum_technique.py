def preprocess(l):
    a=l
    sum=0
    index=0
    for i in a:
        sum+=i
        a[index]=sum
        index+=1
    return a
def sum_left_right(l,left,right):
    if left!=0:

        sum=l[right]-l[left-1]
    else:
        sum=l[right]
    print(sum)
l=[2,8,3,9,6,5,4]
a=preprocess(l)
sum_left_right(a,0,2)
sum_left_right(a,1,3)
sum_left_right(a,2,6)