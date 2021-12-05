# count number of zeros in a string

def count_zero(s,si):
    if si >= len(s)-1:
        if int(s[si]) == 0:
            return 1
        return 0
    c = count_zero(s,si+1)
    if int(s[si]) == 0:
        return c + 1
    else:
        return c

def countzero(n):
    global num
    if n > 0:
        if n % 10 == 0:
            num +=1
        countzero(n//10)
    return num

num = 0
n = int(input("Enter digit: "))
print(count_zero(str(n),0))
print(countzero(n))