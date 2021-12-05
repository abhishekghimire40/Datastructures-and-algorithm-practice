#find maximum and minimum element in an array
# def maxm(c):
    
    # if len(c) == 1:
        # return

c = [5,4,8,9,10,2]
a = 0
b = c[0]
for i in c:
    if i > a:
        a = i
    if b >= i:
        b = i
print(a)
print(b)

    