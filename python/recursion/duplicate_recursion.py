def duplicate(s):
    if len(s) == 1:
        return s
    if s[0] == s[1]:
        smallOutput = duplicate(s[1:])
        if s[0] == smallOutput[0]:
            return smallOutput
    else:
        return s[0] + duplicate(s[1:])
    
print(duplicate('aabbccdd'))

# xxxyyyzwwzzz