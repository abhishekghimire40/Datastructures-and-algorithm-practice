result = []
temp = []


def subsets(nums, i):
    if i == len(nums):
        return result.append([*temp])
    temp.append(nums[i])
    subsets(nums, i + 1)
    temp.pop()
    subsets(nums, i + 1)


subsets([1, 2, 3], 0)
print(result)
