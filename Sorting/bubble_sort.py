def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

l=[10,50,80,20,30]

def optimised_bubble_sort(l):
    for i in range(len(l)):
        swapped=False
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped=True
        if swapped==False:
            return l

print(optimised_bubble_sort(l))