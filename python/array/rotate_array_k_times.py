# Rotate Array by k times
"""
Given an integer array, rotate array to the right by k steps
where k is non-negative 

Input: [1,2,3,4,5], k = 3 ----- Output: [3,4,5,1,2]
Input: [7,9,10,11,12,14] , k = 2 ------- Output: [12,14,7,9,10,11]

Explanation: [1,2,3,4,5,6],k=3 => [6,1,2,3,4,5] => [5,6,1,2,3,4] => [4,5,6,1,2,3]
"""


# Brute force Technique
"""
-- In this approach we first check if k is greater than length of array if then we take
    the remainder using modulo as it won't be a good idea to loop for k times as once
    k == len(arr)  the array will be the same as new array so we take the modulo to reduce steps
--  Then, we are  looping total no. of steps i.e. k  that we have to rotate
    For every step, we traverse our the array once for every step by swapping each item with
    the first item
--  finally returning the array 
--  TimeComplexity: O(m*n)
"""


def rotate_array(arr, k):
    for i in range(k % len(arr)):
        for j in range(len(arr)):
            arr[j], arr[0] = arr[0], arr[j]
    return arr


# Optimized technique
"""
--  we first check if k > len(arr) then take modulo of it to compress it to the array size
--  Then,we take the size i.e. len(arr)  - k.
--  Then, we extract all remaining elements of our array from index of size to last as those
    are the elements that will be shifted to the front after k rotations
    i.e. [1,2,3,4,5], len = 5 , k = 2 then Output: [4,5,1,2,3]
    we can see that 4,5 are the elements from index 3 i.e. len-k = 5-2 = 3 to last
-- So, we can directly extract that element from last and return it to new array
-- we can append all remaining elements of our original array to our new array containing
    those extracted element and return it 
    ELSE:
    we can append the remaining elements to the front of our original array in order
     i.e. order of elements in newArray should be same after appending it to orginal array
       and return it
"""


def rotate_array_optimized(arr, k):
    if k > len(arr):
        k = k % len(arr)
    size = len(arr) - k
    new_arr = arr[size:]
    arr[size:] = []
    for i in arr:
        new_arr.append(i)
    return new_arr


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(rotate_array(arr1, 1))
print(rotate_array_optimized(arr2, 1))
