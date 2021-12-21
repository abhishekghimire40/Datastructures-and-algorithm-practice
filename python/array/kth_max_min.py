#find kth max and min of array

#finding 2nd maximum in o(n)
def max_min(array):
    max = 0
    max_2 = 0
    for i in array:
        if i > max:
            max_2 = max
            max = i
        if i < max and i > max_2:
            max_2 = i
    return max_2

#finding kth max. This is not optimized approach

#in this approach i have found first max of array and skip the max of array for finding the second max
# and skip both the first max and second max for finding 3rd max of array and so on to find the kth max.

def kth_max(array,k):
    max_list = []
    for i in range(k):
        max = 0
        for i in array:
            if i in max_list:
                continue
            if i > max:
                max = i
        max_list.append(max)
    return max
array = [5,6,8,3,2,9,1,11,4,7,10]
k = 3

print(kth_max(array,k)) 
print(max_min(array))