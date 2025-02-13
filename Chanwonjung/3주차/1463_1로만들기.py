#1 그리디로 풀기 (실패)
# num = int(input())
# count = 0

# while num > 1:
#     if num % 3 == 0:
#         num //= 3
#     elif num % 2 == 0:
#         num //= 2
#     else:
#         num -= 1
#     count += 1

# print(count)

#2 DP(다이나믹 프로그래밍) 사용
num = int(input())

#DP 배열 초기화
dp = [0] * (num+1)

#DP 점화식 계산
for i in range(2, num + 1):
    dp[i] = dp[i-1] + 1     #1 뺐을 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)  #3으로 나눴을 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)  #2로 나눴을 때

print(dp[num])
