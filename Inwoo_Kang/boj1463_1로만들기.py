# 1로만들기 s3

x = int(input())

dp = [0, 0, 1, 1]

for i in range(4,x+1):
    dp.append(dp[-1]+1)
    
    if i % 2 == 0 and dp[i//2]+1<dp[i]:
        dp[i] = dp[i//2]+1
        
    if i % 3 == 0 and dp[i//3]+1<dp[i]:
        dp[i] = dp[i//3]+1

print(dp[x])