def left_most_non_repeating_character(s):
        for i in range(len(s)):
            if s[i] not in s[i + 1:]:
                print(i)
                return
        print("-1")


s = "abccb"
left_most_non_repeating_character(s)