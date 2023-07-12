def linear_search(a,b):
    for i in a:
        if i==b:
            return True
    else:
        return False


a=int(input("Element to be searched:"))

l=[10,20,30,40,5,0,50]

if linear_search(l,a):
    print("Found")
else:
    print("Not Found")
