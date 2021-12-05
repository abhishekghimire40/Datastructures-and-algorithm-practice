#code to print the sum of digits

def sum(num,si,ei):
    if si >= ei:
        return num[si]
    
    return int(num[si]) + int(sum(num,si+1,ei))

digit = input("Enter  digit:")
print(sum(digit,0,len(digit)-1))