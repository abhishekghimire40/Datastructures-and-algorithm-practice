n = int(input())


name_numbers = [tuple(input().split(" ")) for i in range(n)]
log = {k:v for k,v in name_numbers}
list1 = []
while True:
    #this will work in test cases  in hacker rank
    try:
        a = input()
        if a in log:
            print(f"{a}={log[a]}")
        else:
            print("Not found")
    except EOFError:
        break

    #this will work in vscode
    # a = input()
    # if a:
    #     if a in log:
    #         print(f"{a}={log[a]}")
    #     else:
    #         print("Not found")
    # else:
    #     break
        
    
