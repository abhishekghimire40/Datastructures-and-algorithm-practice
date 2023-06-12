#given an array of length N find the sum of the array using recursion 

def sum(x):
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]
    return x[0] + sum(x[1:])

#using start index will not make copy of array and occupies less memory space
def isSum(x,si):
    if si == len(x) -1:
        return x[si]
    return x[si] + isSum(x,si+1)

while True:
    n = int(input("Enter the size of an array: "))
    if n == 0:
        print("sum : 0")
        break
    array = input("Enter elements of list: ")
    alist = list(map(int,array.split(" ")))
    if len(alist) == n:   
        print(sum(alist)) 
        print(isSum(alist,0))
        break
    else:
        print(f'Please,Enter array of size {n}.')

