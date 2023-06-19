# Input prices : [7,1,5,3,6,4]


def bestTime(arr):
    if len(arr) <= 1:
        return 0
    low = arr[0]
    maxProfit = 0
    for i in range(len(arr)):
        if arr[i] < low:
            low = arr[i]
            continue
        if arr[i] > low and arr[i] - low > maxProfit:
            maxProfit = arr[i] - low
    return maxProfit


print(bestTime([7, 1, 5, 3, 6, 4]))
print(bestTime([7, 6, 5, 4, 3, 2]))
