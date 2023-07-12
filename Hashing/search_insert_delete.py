from random import randint


def search(d,a):
    if a in d:
        print("Found")
    else:
        print("Not Found")

def insert(d,a,i):
    d[a]=i

def delete(d,a):
    del d[a]
d={}
insert(d,10,randint(0,1000))
insert(d,20,randint(0,1000))
insert(d,119,randint(0,1000))
search(d,10)
search(d,20)
delete(d,119)
search(d,119)