#To find power of a number 
def power(x,n):
    if n == 0:
        return 1
    # if n == 1:
    #     return x 
    return x * power(x,n-1)

x = int(input("enter a number: "))
n = int(input("enter a number to which power is to be raised: "))
print(power(x,n))