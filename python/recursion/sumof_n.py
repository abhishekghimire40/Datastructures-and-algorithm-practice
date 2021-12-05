# To find sum of a natural num from 1 to n
def sum(n):
    if n == 0:
        return 0
    # if n == 1:
    #     return 1
    return n + sum(n-1)
n = int(input())
print(sum(n))