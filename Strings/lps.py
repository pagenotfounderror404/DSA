def lps(s):
    l=[0]
    p=0
    for i in range(1,len(s)):
        a=s[:i]
        if a[p]==s[i]:
            p+=1
            l.append(p)
        else:
            p=0
            l.append(p)


    print(l)

s="abacabad"
lps(s)

