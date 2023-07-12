a=["a","e","i","u"]
r=a.insert(3,"o")

def insertelement(a,i,e):
    s=a[i:]
    a[i]=e
    for i in s:
        a.append(i)
    return a
print(insertelement(a,3,'o'))