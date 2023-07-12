def maxelement(a):
    max=a[0]
    for i in a:
        if i>max:
            max=i

    return a.index(max)

n=int(input("Number of elements: "))
l=[]
print("Enter the elements")
for i in range(n):
    r = int(input())
    l.append(r)

print(maxelement(l))
