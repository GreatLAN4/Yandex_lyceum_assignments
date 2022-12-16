def palindrome(s):
    s, ss = [j for i in s[::-1].lower().split() for j in i],\
            [j for i in s.lower().split() for j in i]
    return "Палиндром" if s == ss else "Не палиндром"
