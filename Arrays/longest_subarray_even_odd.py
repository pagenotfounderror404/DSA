def even(n):
    if n%2==0:
        return True
    else:
        return False


def longest_subarray_even_odd(l):
    res=0
    count=0
    for i in range(1,len(l)):
        if not even(l[i-1]) and even(l[i]):
            if count==0:
                count+=2
            else:
                count+=1
        elif even(l[i-1]) and not even(l[i]):
            if count == 0:
                count += 2
            else:
                count += 1
        else:
            if count>res:
                res=count
            count=0
    if count > res:
        res = count
    return res
l=[7,10,13,14]
print(longest_subarray_even_odd(l))