# print num from 1 to n  and n to 1

def one_to_n(n):
    if n == 0:
        return 
    one_to_n(n - 1)
    print(n)


def n_to_one(n):
    if n == 0:
        return
    print(n)
    n_to_one(n-1)



n = int(input())
one_to_n(n)
print('''
    n to 1:

''')
n_to_one(n)