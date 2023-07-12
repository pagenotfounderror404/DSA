def distinct_character_substring(s):
    a=""
    p=0
    maxi=0
    for i in range(len(s)):
        if s[i] not in a:
            a+=s[i]
            p+=1
            maxi=max(p,maxi)
        else:
            a=""
            p=0
    print(maxi)
s="abcdabc"
distinct_character_substring(s)