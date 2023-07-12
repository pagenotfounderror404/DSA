def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
def lexiographic_rank(s):
    r=0
    for i in range(len(s)):
        p=0
        for j in range(i+1,len(s)):
            if ord(s[i])>ord(s[j]):
                p+=1
        r=r+p*fact(len(s)-i-1)
    print(r+1)

s='string'
lexiographic_rank(s)