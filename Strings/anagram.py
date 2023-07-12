def anagram(a,b):
    d={}
    k={}
    for i in b:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in a:
        if i not in k:
            k[i]=1
        else:
            k[i]+=1
    if k==d:
        print("anagram")
    else:
        print("not an anagaram")

s1="listen"
s2="silent"
anagram(s1,s2)