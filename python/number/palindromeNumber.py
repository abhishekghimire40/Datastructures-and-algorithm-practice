def palindromeNumber(x):
    # guard clauses or edge cases
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    num = 0
    temp = x
    while temp > 0:
        rem = temp % 10
        num = num * 10 + rem
        temp = temp // 10
    return num == x


print(palindromeNumber(121))
print(palindromeNumber(3453))
