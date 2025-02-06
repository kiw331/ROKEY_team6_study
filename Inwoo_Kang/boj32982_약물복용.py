n, k = map(int, input().split())
lst = tuple(map(int, input().split()))

per = lst[1] + k

flag = True
for i in range(n):
    for j in range(3):  #아침 점심 저녁: 01 / 23 / 45
        if per < lst[2*j]:
            flag = False
            break
        
        per = k + min(per, lst[2*j+1])
        
        if j==2:    #저녁->아침 넘어갈때
            per -= 1440
        
    if not flag:
        break

print('YES') if flag else print("NO")