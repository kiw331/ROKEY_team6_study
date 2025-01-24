def sugar_bag(n):
    for five_kg in range(n//5, -1, -1): #n을 5로 나눈 몫부터 
                                        #0까지 역순
        bag = n - (five_kg * 5) #5키로 봉지로 처리하고 
                                #남은 설탕 무게 계산
        if bag % 3 == 0: #남은 무게가 3키로 봉지로 
                         #처리 가능하는지 확인
            three_kg = bag // 3
            return five_kg + three_kg
    return -1

n = int(input())
print(sugar_bag(n))
