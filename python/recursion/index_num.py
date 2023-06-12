#find first and last index of a num in an array.
def firstindex(arr,n,si):
    if si == len(arr)-1:
        if arr[si] == n:
            return si
        else:
            return False
    if len(arr) == si:
        return False
    if arr[si] == n:
        return si
    return firstindex(arr,n,si+1)


def lastindex(arr,n,si):
    if si == 0:
        if arr[si] == n:
            return si
        else:
            return False
    if arr[si] == n:
        return si
    return lastindex(arr,n,si-1)


array = [1,3,4,5,6,2,3,8,9,4]
num = 4
f_index = firstindex(array,num,0)
l_index = lastindex(array,num,len(array)-1)
print(f_index)
print(l_index)