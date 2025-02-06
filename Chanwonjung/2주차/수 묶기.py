def get_max_sum(numbers):
    positive = [] #양수
    negative = [] #음수
    is_zero = False
    
    for num in numbers:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        else:
            is_zero = True
    #양수는 내림차순, 음수는 오름차순으로 정렬
    positive.sort(reverse=True)
    negative.sort()

    result = 0
    #양수(위의 큰 수부터 2개씩 묶기)
    i = 0
    while i < len(positive):
        #1. 다음 수가 존재하고 현재 수가 1보다 크고 다음 수가
        #  1보다 클 때 두수를 곱해서 더함
        if i+1 < len(positive) and positive[i] > 1 and positive[i+1] > 1:
            result += positive[i] * positive[i+1]
            #이후 다음 쌍으로 이동
            i+=2
        else:
            result += positive[i] #조건 불만족 시 그냥 더하고
            i+=1 # 다음 수로 이동
    #음수(작은 수부터 2개씩 묶기)
    i = 0
    while i < len(negative):
        if i+1 < len(negative): #다음 수가 존재하면
            result += negative[i] * negative[i+1] #두 수를 곱하고
            i+=2 #다음 쌍으로 이동
        else: #음수가 하나 남았을 때
            if not is_zero: #0이 없다면
                result += negative[i] #결과값에 음수값을 더함
            i += 1
            
    return result

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

print(get_max_sum(numbers))
            
