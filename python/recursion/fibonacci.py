def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


# using for loop
def fibonacci1(n):
    if n < 2:
        return n
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]


# optimal fibonacci approach
def fibonacciOptimal(n):
    if n < 2:
        return n
    current = 0
    parent = 1
    grandparent = 0
    for i in range(0, n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current


n = int(input())
print(fibonacci(n))
print(fibonacci1(n))
print(fibonacciOptimal(n))
