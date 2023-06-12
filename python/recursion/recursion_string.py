#replace a character with another charracter

def replaceChar(s,a,b): 
    if len(s) == 0:
        return s

    # we can have anyone of the base case.
    # if len(s)  == 1:
    #     if s[0] == a:
    #         return b
    #     else:
    #         return s[0]
    if s[0] == a:
        return b + replaceChar(s[1:],a,b)
    else:
        return s[0] + replaceChar(s[1:],a,b)



print(replaceChar("cxxxcsadfaksdjxcxc","c","x"))
