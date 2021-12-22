#move all the zeroes present in the array to the end of the array maintaining the order

#this is the first that i have done:
#this is not an optimized approach
#I created a new array and traverse through the original array and if the element is 
#non-zero then i appended it into the array and if the element is zero then i count the number
#of zeroes present in the array and finally run a loop from 1 to count and appended the total no of
#zeros in the new array which gives the answer.
array1 = [1,0,2,0,3,0,0,0,5,6,7,9,0]
count_zeroes = 0
new_array = []
for i in array1:
    if i:
        new_array.append(i)
    else:
        count_zeroes += 1
for i in range(count_zeroes):
    new_array.append(0)
print(new_array)



#In this approach we traverse the array, also take a pointer a which points at the first element at first
#and everytime a non zero element comes, we swap the element with the element at position a and increase
#the value of a.
#this is an optimized approach
def swap(array,i,a):
    array[i],array[a] = array[a],array[i]
    return
array = [1,0,2,0,3,0,0,0,5,6,7,9,0]
a = 0 
for i in range(len(array)):
    if array[i]:
        swap(array,i,a)
        a += 1
print(array)