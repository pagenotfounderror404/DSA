def sub_sequence(a,b):
    p=0
    for i in range(len(a)):
        if a[i]==b[p]:
            p+=1

    if p!=len(b):
        print("not a sub sequence")
    else:
        print("is a sub sequence")

s1="ABCDE"
s2="ADE"
sub_sequence(s1,s2)

