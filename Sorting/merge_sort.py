
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]


        merge_sort(L)


        merge_sort(R)

        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# FAILED
# def merge(l,r):
#     s=0
#     p=r+1
#     pointer=0
#     k=[]
#
#     while(pointer<len(l)):
#         if p >=len(l):
#             for i in range(s, r):
#                 k.append(l[i])
#                 break
#         elif s >= r+1:
#             for i in range(p,len(l)):
#                 k.append(l[i])
#             break
#         if l[s]>l[p]:
#             k.append(l[p])
#             p+=1
#             pointer+=1
#         elif l[p]>l[s]:
#             k.append(l[s])
#             s+=1
#             pointer+=1
#         elif l[s]==l[p]:
#             k.append(l[s])
#             k.append(l[p])
#             s+=1
#             p+=1
#             pointer+=2
#     l=k
#     return l
# def merge_sort(l,lb,ub):
#     if len(l) > 1:
#             mid = len(l) // 2
#             merge_sort(l,0,mid)
#             merge_sort(l,mid+1,len(l))
#             merge(l,mid)


l=[5,30,10,15,60,20]
merge_sort(l)
print(l)

