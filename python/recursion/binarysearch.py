#code for binary search using recursion 

def binarysearch(l,si,ei,n):
    # if si == ei:
    #     if l[si] == n:
    #         return si 
    #     else:
    #         return False
    if si > ei :
        return False    
    m = round((si + ei)/2)
    if n == l[m]: #basecase
        return m
    elif n > l[m]:
        return binarysearch(l,m+1,ei,n)
    else:
        return binarysearch(l,si,m-1,n)

print(binarysearch([1,2,3,4,5],0,4,2))