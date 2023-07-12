def palin(s, j,i=0):

    if j-i==1 or i==j:
        return True
    return palin(s,j-1,i+1) and s[i]==s[j]

s=input("Enter s: ")
j=len(s)-1
print(palin(s,j))