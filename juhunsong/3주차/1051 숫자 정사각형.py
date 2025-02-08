n,m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

for i in range(min(n,m), 0, -1):
    for k in range(0,m-i+1):
        for j in range(0,n-i+1):
            if matrix[j][k] == matrix[j+i-1][k] == matrix[j][k+i-1] == matrix[j+i-1][k+i-1]:
                print(i*i)
                exit()

print(1)
    