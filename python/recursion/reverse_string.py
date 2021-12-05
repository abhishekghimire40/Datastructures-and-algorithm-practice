def reverseWord(s,si):
    #your code here
    if si == len(s) - 1:
        return s[si]
    return reverseWord(s,si+1) + s[si]

print(reverseWord("Doshim",0))   