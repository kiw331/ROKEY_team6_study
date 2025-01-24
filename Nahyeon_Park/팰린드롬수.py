# 팰린드롬수(앞 뒤가 같은 수)


num_list = []               #입력받을 숫자를 저장할 리스트

# <숫자 입력받기>
# 1<=num<=99999 
while True:
    try:
        num = input()
        if num == '0':          # '0' 입력하면 탈출
            break

        if not num.isdigit():   # 숫자가 아닌 값이 입력된 경우
            raise ValueError("숫자를 입력하세요.")
    
        num = int(num)          # 입력값을 정수로 변환

        if num <= 1 or num >= 99999:  # 조건에 맞지 않으면 오류 발생
            raise ValueError("1보다 크고 99999보다 작은 숫자를 입력하세요.")
        
        num_list.append(str(num))   # 입력받은 숫자 넣어주기

    except ValueError as e:
        print(e)


result_list = []            # 결과값 리스트


# <앞뒤가 똑같은지 계산하기>
# num_list에서 값(문자열) 하나씩 꺼내오기
for num in num_list:
    # (문자열 길이//2)만큼 돌아가기  /// ex) '12321' -> 2번, '5894' ->2 번   
    for i in range(len(num)//2):            # 단어의 반만 돌기
        if num[i] == num[len(num)-1-i]:     # 왼쪽끝, 오른쪽끝 같은지 비교 ///중요한건 우항 -1
            result = 'yes'                  # 양쪽 끝이 같다면 'yes' 저장
        else:                               # 다르다면 
            result = 'no'                   # 'no'저장후 반복문 빠져나가기
            break
    result_list.append(result)              # 값 하나 돌때마다 상태 저장

print('---------------')
# <결과 출력>
for i in result_list:
    print(i)
