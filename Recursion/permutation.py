
def toString(List):
    return ''.join(List)

def permutation(s,i=0):
    if i==int(len(s)-1):
        print(toString(s))
        return
    for j in range(i,len(s)):
        s[i],s[j]=s[j],s[i]
        permutation(s,i+1)
        s[i],s[j]=s[j],s[i]


a=input("Enter a string")
s=list(a)

permutation(s)