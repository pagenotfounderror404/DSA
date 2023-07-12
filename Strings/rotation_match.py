def rotation_match(s,r):
    for i in range(len(s)):
       p=s[len(s)-i:]+s[:len(s)-i]
       if p==r:
           print("Yes")
           return
    print("No")



def rotation_match_efficient(s,r):
    p=0
    k=0
    for i in range(len(s)):
        if s[i]==r[p]:
            p+=1
            if i==len(s)-1:
                k=i-p+1

    m=s[k:]+s[:k]
    if m==r:
        print("Yes")
    else:
        print("No")


s = "abaaa"
r = "baaaa"
rotation_match_efficient(s, r)