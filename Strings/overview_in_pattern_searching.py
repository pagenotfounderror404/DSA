def overview_in_pattern_searching(s,a):
    p=len(a)
    if a in s:
        for i in range(len(s)):
            if s[i:i+p]==a:
                print(i, end=" ")
        return
a="geeksforgeeks"
overview_in_pattern_searching(a,"eks")