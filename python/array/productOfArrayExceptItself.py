"""
238. Product of Array Except Self: (Medium)
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


# Done by me
#  with division operator
def productExcepSelf(nums):
    prod = 1
    containsZero = False
    multipleZero = False
    for i in nums:
        if containsZero and i == 0:
            multipleZero = True
            continue
        if i == 0:
            containsZero = True
            continue
        prod *= i
    if multipleZero:
        return [0 for i in nums]
    if containsZero:
        return [prod if i == 0 else 0 for i in nums]
    return [prod // i for i in nums]


# wihtout using division:
def productExceptSelfOptimized(nums):
    prefix = 1
    postfix = 1
    output = []
    for i in nums:
        output.append(prefix)
        prefix *= i
    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * postfix
        postfix *= nums[i]
    return output


print(productExcepSelf([1, 2, 3, 4]))
print(productExceptSelfOptimized([1, 2, 3, 4]))
