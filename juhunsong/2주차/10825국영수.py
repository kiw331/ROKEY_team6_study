import sys
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(sys.stdin.readline().split()))
    arr[i][1] = int(arr[i][1])
    arr[i][2] = int(arr[i][2])
    arr[i][3] = int(arr[i][3])

arr.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for i in range(n):
    print(arr[i][0])
