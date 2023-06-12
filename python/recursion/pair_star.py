#Given a string S, compute recursively a new string where identical
#  chars that are adjacent in the original string are separated from each other by a "*".


def star(s,si):
    if si >= len(s)-1:
        return s[si]
    c = star(s,si+1)
    if s[si] == c[0]:
        return s[si]+"*"+c
    else:
        return s[si]+c

word = input("Enter a word: ")
print(star(word,0))

