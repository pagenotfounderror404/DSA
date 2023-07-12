def k_largest_element(arr,k):
    for i in range(k):
        print(max(arr),end="")
        arr.remove(max(arr))