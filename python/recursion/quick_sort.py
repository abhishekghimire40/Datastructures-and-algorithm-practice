#code for quick sort


def partition(arr,si,ei):
    n = 0
    i = si
    a = arr[si]
    # for i in range(si,ei):
    #     if a > arr[i+1]:
    #         n = n+1
    while i < ei:
        if a > arr[i+1]:
            n = n+1
        i = i+1
    arr[si],arr[si+n] = arr[si+n],arr[si]
    count = si + n
     
    while si < ei :
        if arr[si] < arr[count]:
            si = si + 1
        elif arr[ei] >= arr[count]:
            ei = ei-1
        else:
            arr[si],arr[ei] = arr[ei],arr[si]
            si = si+1
            ei = ei-1
    return count





def quick_sort(arr,si,ei):
    if si >= ei:
        return
    c = partition(arr,si,ei)
    quick_sort(arr,si,c-1)
    quick_sort(arr,c+1,ei)
    



arr = [10,6,100,5,96,33,1,3,4,20,1,9,7,2]
quick_sort(arr,0,len(arr)-1)
print(arr)
