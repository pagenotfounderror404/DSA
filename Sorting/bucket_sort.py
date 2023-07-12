def insertionSort(l):
    for i in range(1, len(l)):
        key = l[i]
        for j in range(i):
            if l[i] < l[j]:
                del l[i]
                l.insert(j, key)
                break
    return l


def bucketSort(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])

    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
