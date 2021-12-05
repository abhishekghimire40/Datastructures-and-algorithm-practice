# def fact(n):
#     if n == 0:
#         return 1
#     # y = fact(n-1)
#     return n * fact(n-1)

    
# n = int(input())
# factorial = fact(n)
# print(factorial)
import sys
sys.setrecursionlimit(3000)

def DPfact(N):
    arr={}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
    else:
        factorial = N*DPfact(N - 1)
        arr[N] = factorial
    return factorial

num=int(input("Enter the number: "))
print("factorial of ",num," (dynamic): ",end="")
print(DPfact(num))