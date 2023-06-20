"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

from collections import defaultdict


# Brute force method
def kFrequent(nums, k):
    count = {}
    el = []
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in range(k, 0, -1):
        max = float("-inf")
        maxKey = ""
        for key, val in count.items():
            if val > max:
                max = val
                maxKey = key
        del count[maxKey]
        el.append(maxKey)
    return el


# Linear time using Bucket sort:
def kFrequentOptimized(nums, k):
    count = {}
    el = []
    res = [[] for x in range(len(nums) + 1)]
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1
    for key, val in count.items():
        res[val].append(key)
    for i in range(len(nums) - 1, 0, -1):
        for j in res[i]:
            el.append(j)
            if len(el) == k:
                return el
    return el


# print(kFrequent([1, 1, 1, 2, 2, 3], 2))
# print(kFrequent([1], 1))
print(kFrequentOptimized([1, 1, 1, 2, 2, 3], 2))
print(kFrequentOptimized([1], 1))
