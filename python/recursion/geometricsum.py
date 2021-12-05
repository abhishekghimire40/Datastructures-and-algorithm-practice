#code to calculate geometric sum using recursion 

def gSum(n):
    if n < 1:
        return 1
    a = 1/(2**n)
    return a + gSum(n-1)

n = int(input())
print(gSum(n))


