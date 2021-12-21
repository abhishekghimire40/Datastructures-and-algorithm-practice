#traverse the array and compare elements and save max of each comparision until it traverses the whole array
def max_min(array):
    max = 0
    min = array[0]
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
    return max,min
array = [5,6,8,3,2,10,1,11,4,7,9]
print(max_min(array))
max = 0
min = 0
# for i in range(len(array)):
#     si = i+1
#     if si == len(array):
#         break
#     if array[i] > array[si]:
#         max = array[i]
#     else:
#         max = array[si]
print(max)
