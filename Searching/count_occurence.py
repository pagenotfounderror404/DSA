from last_occurence import binary_search_last_occurence
from first_occurence import binary_search_first_occurence
def count_occurence(l,e):
    f=binary_search_first_occurence(l,e)
    l=binary_search_last_occurence(l,e)
    if f==-1 or l==-1:
        print("No element found")
    else:
        print(l-f+1)

x=20
l=[5,10,15,20,20,20,20]
count_occurence(l,x)