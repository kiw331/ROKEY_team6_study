#기본적인 문법 사용
import sys

#A = 올라가는 높이, B = 미끄러지는 높이, V = 전체 길이
# 올라가야할 높이 = V - B, 하루에 갈 수 있는 높이 = A - B

input = sys.stdin.readline
A, B, V = map(int, input().split())   

if (V - B) % (A - B) == 0:
    print((V - B) // (A - B))
else:
    print((V - B) // (A - B) + 1)

#ceil 함수 사용
import math
import sys
input = sys.stdin.readline
A, B, V = map(int, input().split())   
day = (V - B) / (A - B)
print(math.ceil(day)) #ceil = 실수를 입력하면 올림하여 정수를 반환
