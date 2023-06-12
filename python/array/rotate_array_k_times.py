# Rotate Array by k times
"""
Given an integer array, rotate array to the right by k steps
where k is non-negative 

Input: [1,2,3,4,5], k = 3 ----- Output: [3,4,5,1,2]
Input: [7,9,10,11,12,14] , k = 2 ------- Output: [12,14,7,9,10,11]

Explanation: [1,2,3,4,5,6],k=3 => [6,1,2,3,4,5] => [5,6,1,2,3,4] => [4,5,6,1,2,3]
"""


# Brute force Technique
def rotate_array(arr, k):
    for i in range(k % len(arr)):
        for j in range(len(arr)):
            arr[j], arr[0] = arr[0], arr[j]
    return arr


# Optimized technique
def rotate_array_optimized(arr, k):
    if k > len(arr):
        k = k % len(arr)
    size = len(arr) - k
    new_arr = arr[size:]
    arr[size:] = []
    for i in range(len(new_arr), 0, -1):
        arr.insert(0, new_arr[i - 1])
    return arr


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(rotate_array(arr1, 1))
print(rotate_array_optimized(arr2, 1))
