import sys

input = sys.stdin.readline #속도 향상
n = int(input())
age_list = []

for i in range(n):
    age, name = map(str, input().split())
    age_list.append((int(age), name)) # append는 하나의 인자만 입력받기 때문에 튜플로 추가

age_list.sort(key = lambda x : x[0]) 

for i in age_list:
    print(i[0], i[1])

    