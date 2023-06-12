# Suppose you have a string, S, made up of only 'a's and 'b's.
#  Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.

def check(si,s):
    if si > len(s) - 1:
        return True
    if si == 0:
        if s[si] == "a":
            pass
        else:
            return False
    if s[si] == "a":
        if s[si+1] == "":
            pass
        elif s[si+1] == 'a':
            pass
        elif s[si+1] == "b":
            try:
                if s[si+2] == "b":
                    pass
            except:
                return False
        else:
            return False

    if s[si] == "b" and s[si-1] == "b":
        if s[si+1] == "" or s[si+1] == "a":
            pass
        else:
            return False
    elif s[si] == "b" and s[si+1] == "b":
    