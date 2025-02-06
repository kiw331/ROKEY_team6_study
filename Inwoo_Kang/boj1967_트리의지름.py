# 실패

n = int(input())

edge = []
for i in range(n-1):
    p, c, w = map(int, input().split())
    edge.append([p, c, w])