
def hash_function(l:int):
    return int(l%7)
l=[[] for i in range(7)]
m=[70,71,9,56,72]
def insert(l,i):
    key=hash_function(i)
    l[key].append(i)
def delete(l,a):
    key = hash_function(a)
    l[key].remove(a)
def search(l,a):
    key=hash_function(a)
    if a in l[key]:
        print("Found")
    else:
        print("Not Found")

