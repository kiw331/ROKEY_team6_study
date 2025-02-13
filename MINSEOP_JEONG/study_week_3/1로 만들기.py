import sys

input = sys.stdin.readline
x = int(input().strip())
count = 0

while x > 1:
    if x % 3 == 0:
        x /= 3
        count += 1
    elif x & 2 == 0:
        x /= 2
        count += 1
    else:
        x -= 1
        count += 1

print(count)
## 런타임 에러


# dp 풀이
x=int(input()) # 수 입력받기
d=[0]*(x+1) # 1-based
for i in range(2,x+1): # 2부터 x까지 반복
    d[i]=d[i-1]+1 # 1을 빼는 연산 -> 1회 진행
    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i]=min(d[i],d[i//3]+1)
print(d[x])
