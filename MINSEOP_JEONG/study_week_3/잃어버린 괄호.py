arr = input().split('-')
m = 0

for i in arr[0].split('+'):
    m += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        m -= int(j)

print(m)