#1. find second max of array

"""
First approach is to traverse the array and find the maximum once and again 
traverse the array and ignore the element which is the max and find the max among remaining 
elements
"""
def secondLargest(arr):
    max = float('-inf')
    for i in arr:
        if i > max:
            max = i
    secondMax = float('-inf')
    for i in arr:
        if i == max:
            continue
        if i > secondMax:
            secondMax = i
    return secondMax

"""
Another approach is to use sorting algorthim and once sorted we can extract the any largest element
from array.
NOTE:
But the catch is if there is repeated element like if there are multiple same numbers i.e.
if there is two 35 that is max number then when sorted second place from the last will also be 
35 as there are two 45 but 35 willnot be out second largest element. So for this case
we can first convert the list into set so that every element is unique then after sorting we 
can get the required largest element

ALSO: we can use any sort mainly of O(nlogn) or use builtin sorted or sort method

Time Complexity : O(nlogn)
"""

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = arr // 2 
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    return merge(left_sorted,right_sorted)

def merge(left,right):
    i = 0
    j = 0
    newArr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            newArr.append(left[i])
            i+=1
        else:
            newArr.append(right[j])
            j += 1
    while i < len(left):
        newArr.append(left[i])
        i += 1
    while j < len(right):
        newArr.append(right[j])
        j += 1
    return newArr


"""
OPTIMISED APPROACH:
 - First we initialized the max and second max with negative infinity
 - Then we traverse the array, and check if array at current index is greater than
    max or not. If greater then initalize second max to max and current element as current max
    Also. if current element is not greater than or equal to max then if current element is
    greater than second max if so set second max to current element and leave max as it is
 - Return the second max after completing the traverse of that array
"""
def SecondLargestOptimized(arr):
    max = float('-inf')
    secondMax = float('-inf')
    for i in arr:
        if i > max:
            secondMax = max
            max = i
        elif i != max and i > secondMax:
            secondMax = i
    return secondMax

array_12 = [9, 6, 12, 3, 11, 2, 10, 8, 5, 1, 7, 4]
print(secondLargest(array_12))
print(SecondLargestOptimized(array_12))