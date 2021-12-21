# def array_reverse(array,array1,si):
#     if si >=len(array)-1:
#         return array[si]
#     array1.append(array_reverse(array,array1,si+1))
#     return array[si]

def array_re(array,array1,si):
    if si >= len(array)-1:
        array1.append(array[si])
        return
    array_re(array,array1,si+1)
    array1.append(array[si])
    return 

def array_swap(array,si,ei):
    while si != ei:
        array[si],array[ei] = array[ei],array[si]
        si += 1
        ei -= 1
    return array

def array_reverse_loop(array):
    for i in range(len(array)-1,-1,-1):
        array1.append(array[i])
    print(array1)

array = [10,6,5,3,7,8,9]
array1 = []

# array_reverse(array,array1,0)
# print(array1)
# print(array_swap(array,0,len(array)-1))
# array_reverse_loop(array)
array_re(array,array1,0)
print(array1)
