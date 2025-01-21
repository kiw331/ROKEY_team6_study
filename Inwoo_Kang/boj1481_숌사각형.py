# 숌사각형 g3
from itertools import permutations

n,d = map(int, input().split())

rows = [[0]*(n-d) + list(range(d))] * (n-d+1)   #0행~(n-d+1)행
for i in range(1,d):  #n-d행~
    rows.append([i]*(n-d)+list(range(d)))
    
# 모든 열이 유효한지 확인
def is_vaild(row):    
    for col in range(n):
        lst = [mat[r][col] for r in range(row+1)]

        # row행까지왔을 때 있어야하는 (중복없는)최소 원소 개수 
        if len(set(lst)) <= row-(n-d):
            return False
    return True
    
mat = [[] for _ in range(n)]    #정답 저장할 2차원 리스트
for i in range(n):
    row = sorted(rows[i])
    
    for c in permutations(row):
        if c[0] != max(0,i-(n-d)):  #수열의 첫번째 숫자 확인(시간초과 방지)
            continue
        
        mat[i] = c
        
        if is_vaild(i):
            break

for row in mat:
    print(*row)            
        