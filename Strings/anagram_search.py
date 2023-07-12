def anagram_search(s,a):
    l=len(a)
    p=1
    for i in range(len(s)):
        for j in range(len(a)):
            if a[j] in s[i:i+l]:
                p+=1
            else:
                p=1
        if p==l:
            print("yes")
            return
    print("no")


def anagram_search_efficient(s,a):
    l=len(a)
    p=1
    k=1
    for i in range(len(s)):
        if s[i]==a[0]:
            for j in range(len(a)):
                if a[j] in s[i-l+1:i+1]:
                    p+=1
                if a[j] in s[i:i+l]:
                    k+=1
                if p == l or k == l:
                    print("Yes")
                    return
            p=1
            k=1

    print("No")

g="geeksforgeeks"
r="frog"
anagram_search_efficient(g,r)