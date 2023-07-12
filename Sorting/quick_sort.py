from partitioning import loumo_partition,hoare_partition2


def quick_sort_using_loumuto_partition(l,low,high):
    if (low<high):
        p=loumo_partition(l,low,high)
        quick_sort_using_loumuto_partition(l,low,p-1)
        quick_sort_using_loumuto_partition(l,p+1,high)









def quicksort(a, low, high):

    if low >= high:
        return


    pivot = hoare_partition2(a, low, high)

    quicksort(a, low, pivot)

    quicksort(a, pivot + 1, high)


l=[8,1,3,4,6,9,5,7,9,6]
quicksort(l,0,len(l)-1)
print(l)
