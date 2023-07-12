sets=[]
def subset(n, l, sum):
    if n==0:
        # r=string_to_list(c,',')
        # sets.append(r)
        if sum==0:
            return 1
        else:
            return 0
    return subset(n - 1, l, sum)+subset(n - 1, l,sum-l[n-1])


def string_to_list(n,c):
    l=list(n.split(c))
    return l

l=[]
n=int(input("Enter the number of elements"))
for i in range(n):
    a=int(input(f"Enter the {i+1} element"))
    l.append(a)

sum=int(input("Enter the sum"))

print(subset(n,l,sum))

# subset(n, l)
# print(sets)
#
# k=0
# p=0
# for i in sets:
#     for j in i:
#         if j == "":
#             l[k][p] = int(0)
#         else:
#             l[k][p] = int(j)
#         p+=1
#     k+=1
#
# print(sets)