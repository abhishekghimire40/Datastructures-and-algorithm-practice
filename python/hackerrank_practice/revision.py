# revising reccursion

#1. Mergesort

def merge(a1,a2,arr):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] > a2[j]:
            arr[k] = a2[j]
            j += 1
            k += 1
        else:
            arr[k] = a1[i]
            i += 1
            k += 1

    while i < len(a1):
        arr[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        arr[k] = a2[j]
        j += 1
        k += 1

def mergesort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    mergesort(arr1)
    mergesort(arr2)
    merge(arr1,arr2,arr)


arr = [1,3,6,9,2,4,5,10,12]
mergesort(arr)
print(arr)


#2.quicksort

import time
def partition(arr,si,ei):
    p = arr[si]
    j = 0
    for i in range(ei+1):
        if p > arr[i]:
            j += 1
    arr[si],arr[j] = arr[j],arr[si]
    while ei > si:
        if arr[si] > p:
            if arr[ei] < p:
                arr[si],arr[ei] = arr[ei],arr[si]
                si += 1
                ei -= 1
            else:
                ei -= 1
        else:
            si += 1
    return j 

def quicksort(arr,si,ei):
    if si >= ei:
        return
    i = partition(arr,si,ei)
    quicksort(arr,si,i-1)
    quicksort(arr,i+1,ei)

arr = []
for i in range(1000,0,-1):
    arr.append(i)
start = time.time()
quicksort(arr,0,len(arr)-1)
end = time.time()
print(end - start)


#3.factorial

def fact(n):

    #using recursion
    if n == 1 or n == 0 :
        return 1
    return n * fact(n-1)

    #using loop
    f = 1
    for i in range(n,0,-1):
        f = f * i
    return f

num = int(input("Enter a num: "))
print(fact(num))


# 4.Sum_of_digits
def sum_of_digits(n):
    #basecase(
    if n <= 0:
        return 0

        #or

    if n % 1 == n:
        return n
        #)
    sum = n % 10
    return sum + sum_of_digits(n//10)

num = int(input("Enter a number: "))
print(sum_of_digits(num))

#5.multiple_of_digits

def mul_of_digits(n):
    
    # using recursion
    if n % 10 == n:
        return n
    mul = n % 10
    return mul * mul_of_digits(n//10)

    # using for loop
    mul = 1
    for i in range(len(str(n))):
        mul = mul * (n % 10)
        n = n // 10
    return mul

num = int(input("Enter a number: "))
print(mul_of_digits(num))



#print repeating characters
def repeat(s):
    new = ""
    ex= []
    for i in s:
        if i in ex:
            new += i
        else:
            ex.append(i)
    return new

n = "abhishek"
print(repeat(n))


#move zeros to last of array
def move_zeros(a,si,ei):
        while si <= ei:
            if a[si] == 0:
                if a[ei] != 0:
                    a[si],a[ei] == a[ei],a[si]
                else:
                    ei -= 1
            else:
                si += 1
        return a

a = [1,0,2]
print(move_zeros(a,0,len(a)-1))