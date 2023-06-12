#check whether a number is palindrome or not

def palindrome(s,si,ei):
    if si >= ei:
        return True
    if s[si] == s[ei]:
        return palindrome(s,si+1,ei-1)
    else:
        return False

word = input("Enter a word to check if the number is palindrome or not: ")
print(palindrome(word,0,len(word)-1))