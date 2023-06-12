#code for tower of hanoi 

def hanoi(n,start,helper,final):
    if n == 1:
        print(f"{start}>{final}")
        return
    hanoi(n-1,start,final,helper)
    print(f"{start}>{final}")
    hanoi(n-1,helper,start,final)

n = 4   
hanoi(n,"A","B","C")
    
    
