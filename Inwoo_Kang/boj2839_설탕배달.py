# 설탕 배달 s4
n = int(input())
INF = float('inf')
lst = [INF] * (n+3)    # n이 인덱스가 되는 최소봉지 리스트(ex lst[10] = 10kg일 때 최소봉지개수)
lst[3], lst[5] = 1, 1

for i in range(6,n+1):
    lst[i] = min(lst[i-5], lst[i-3]) + 1

print(lst[n] if lst[n]!=INF else -1)