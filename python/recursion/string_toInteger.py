#convert string to integer

def string_integer(num,si):
    if si >= len(num)-1:
        return int(num[si]),1
    c,p = string_integer(num,si+1)
    return int(num[si])*(10**p) + c ,p+1

def stringInteger(n,si):
    if si>=len(n)-1:
        return n[si]
    c = stringInteger(n,si+1)
    return int(n[si])*(10**((len(n)-1)-si)) + int(c)

digit = str(input("Enterdigit: "))
print(type(digit))
value = string_integer(digit,0)
val = stringInteger(digit,0)
print(f"{value[0]}, type:{type(value[0])}")
print(val)