#print multiplication value of a x b using recursion. I can only  use addition and subtraction operator

def multiplication(num1,num2):
    if num2 == 1:
        return num1
    if num1 == 0 or num2 == 0:
        return 0
    return num1 + multiplication(num1,num2-1)

a = int(input("First num: "))
b = int(input("second num: "))
if a > b:
    print(multiplication(a,b))
else:
    print(multiplication(b,a))
    
