def left_most_repeating_character(s):
        for i in range(len(s)):
            if s[i] in s[i+1:]:
                print(i)
                break
s="abccb"
left_most_repeating_character(s)