from sys import stdin, exit

n, m = map(int, stdin.readline().split())
lst = [stdin.readline() for _ in range(n)]
        
for i in range(min(n,m), 0, -1):
    for y in range(n-i+1):
        for x in range(m-i+1):
            if lst[y][x] == lst[y+i-1][x] == lst[y][x+i-1] == lst[y+i-1][x+i-1]:
                exit(print(i**2))