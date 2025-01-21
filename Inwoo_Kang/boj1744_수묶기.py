# 수 묶기 g4
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst = sorted(lst) + [0] # 요소 한개 일때 인덱스 에러 방지
dp = [lst[0], max(lst[0]+lst[1],lst[0]*lst[1])]

for i in range(2,n):
    dp.append(max(dp[i-2]+lst[i-1]*lst[i], dp[i-1]+lst[i]))
    
print(dp[n-1])