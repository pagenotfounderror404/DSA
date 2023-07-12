l=[None for i in range(7)]
def hash_function(l:int):
    return int(l%7)
def insert(l,a):
    key=hash_function(a)
    for i in range(key,len(l)+key):
        if l[key%len(l)] is None or l[key%len(l)]=='deleted':
            l[key%len(l)]=a
def search(l,a):
    key=hash_function(a)
    for i in range(key,len(l)+key):
        if l[key%len(l)]==a:
            print("Found")
            break
        if l[key%len(l)]==None:
            print("not found")
            break
def delete(l,a):
    key=hash_function(a)
    for i in range(key,len(l)+key):
        if l[key%len(l)]==a:
            l[key % len(l)] = 'deleted'
            break