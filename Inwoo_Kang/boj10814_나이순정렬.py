n = int(input())
lst = []

for i in range(n):
    age, name = input().split()
    lst.append([int(age),name])
lst.sort(key=lambda x: x[0])

for i in range(n):
    print(*lst[i])