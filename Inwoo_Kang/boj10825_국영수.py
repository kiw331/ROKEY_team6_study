# boj10825_국영수 s4
lst = []
for _ in range(int(input())):
    name, 국, 영, 수 = input().split()
    lst.append((name,int(국), int(영), int(수)))

# 정렬 기준 설정: 내림, 오름, 내림, 오름
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in lst:
    print(i[0])