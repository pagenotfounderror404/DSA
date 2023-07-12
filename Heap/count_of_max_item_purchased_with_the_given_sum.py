def max_item(a,sum):
    s=0
    min_item = min(a)
    while sum>=min_item:
        sum-=min_item
        s+=1
        a.remove(min_item)
        min_item = min(a)
    print(s)
cost=[20,10,5,30,100]
max_item(cost,35)