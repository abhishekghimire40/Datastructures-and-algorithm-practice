
#minimun characters to be added to make the string palindrome

# def palindrome(s):
#     a = len(s)//2
#     for i in range(a):
#         if s[i] == s[len(s)-i-1]:
#             b = True
#         else:
#             b = False
#             break

#     if b:
#         return True
#     else:
#         return False




def palindrome_recursion(s,si,ei):
    if  si == ei:
        return True
    if s[si] == s[ei]:
        return palindrome_recursion(s,si+1,ei-1)
    else:
        return False

def append(s):
    if palindrome_recursion(s,0,len(s)-1):
        return ""
    
    return  append(s[1:]) + s[0]




s = "lnmjarcr"
print(append(s))
