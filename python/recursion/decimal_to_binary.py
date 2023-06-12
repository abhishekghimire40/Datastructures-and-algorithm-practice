import math

def binary(n):
    if n == 0 or n == 1:
        return n
    a = math.floor(n/2)
    smallOutput = str(binary(a))
    return smallOutput + str(n%2) 

def count(s,si):
    if si == len(s)-1:
       return int(s[si])
    smallCount = int(count(s,si+1))
    if si == 0:
        if s[si] == "1":
            max_list.append(smallCount+1)
            return
        else:
            max_list.append(smallCount)
    if smallCount >= 1:
        if s[si] == "1":
            return smallCount + 1
        else:
            max_list.append(smallCount)
            return 0
    if smallCount == 0:
        if s[si] == "1":
            return 1
        else:
            return 0

num = int(input())
max_list = []
a = binary(num)
count(a,0)
print(max(max_list))











#  if s[si] == 1:
#             return 1
#         else:
#             return 0
#     smallCount = count(s,si+1)
#     if smallCount >= 1:
#         if si == 0:
#             if s[si] == "1":
#                 max_list.append(smallCount+1)
#             else:
#                 max_list.append(smallCount)
#         if s[si] == "1":
#             return smallCount + 1
#         else:
#             max_list.append(smallCount)
#             return 0
#     else:
#         if s[si] == "1":
#             return 1
#         else:
#             return 0


