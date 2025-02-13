#10814 나이순 정렬
a=int(input())
l=[]
for i in range(a):
  l.append(list(input().split()))
l.sort(key = lambda x: int(x[0]))

for i in l:
  print(i[0],i[1])