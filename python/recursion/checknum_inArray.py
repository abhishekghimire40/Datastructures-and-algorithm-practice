def checknum(arr,x,si):
    if si == len(arr) -1:
        return arr[si] == x
    if arr[si] == x:
        return True
    return checknum(arr,x,si+1)       
    


n = int(input("Enter the size of an array: "))
array = input("Enter the elements of array separated by space: ")
num = int(input("Enter the number you want to check: "))
alist = list(map(int,array.split(" ")))
if len(alist) == n:
    print(checknum(alist,num,0))

