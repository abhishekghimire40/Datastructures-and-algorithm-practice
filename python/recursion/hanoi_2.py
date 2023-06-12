def hanoi(n,start,helper,end):
    if n == 1:
        print(f"{n}[{start} -> {end}]")
        return
    hanoi(n-1,start,end,helper)
    print(f"{n}[{start} -> {end}]")
    hanoi(n-1,helper,start,end)
    return

num = 3
hanoi(num,"10","12","11")