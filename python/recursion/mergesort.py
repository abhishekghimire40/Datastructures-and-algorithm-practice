#code for merge sort
import math

def merge(a,b,arr):
    i = 0 
    j = 0 
    k = 0 
    while i < len(a) and j< len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i = i + 1
            k = k + 1
        else:
            arr[k]=b[j]
            j = j+1
            k = k+1
    while i < len(a):
        arr[k] = a[i]
        i = i+1
        k = k+1
    while j < len(b):
        arr[k] = b[j]
        j = j+1
        k = k+1


def mergesort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = math.floor(len(arr)/2)
    arr1 = arr[0:mid]
    arr2 = arr[mid:]
    mergesort(arr1)
    mergesort(arr2)
    merge(arr1,arr2,arr)

arr = [7,2,9,3,10,6,5,1,8,4]
mergesort(arr)
print(arr)
