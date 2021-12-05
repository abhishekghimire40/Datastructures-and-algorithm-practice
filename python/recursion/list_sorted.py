# check if the list is sorted or not by recursion.

#this will create a multiple copy of array which is not  good for memory space allocation 
def sort(x):
    if len(x) == 0 or len(x) == 1:
        return True
    if x[0] > x[1]:
        return False
    else:
        return sort(x[1:])

#using start index will occupy small memory as it has only one array
def isSorted(arr,si):
    if si == len(arr) - 1 or si == len(arr):
        return True
    if arr[si] > arr[si+1]:
        return False
    return isSorted(arr,si+1)


sort_list = [1,1,3,4,5,7,20,9,14,15,16]
isort_list = [1,1,3,4,5,7,8,9,14,15,16]
print(sort(isort_list))
print(isSorted(sort_list,0))