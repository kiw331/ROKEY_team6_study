# 상근이의 설탕배달!

# <예외처리>
while True:
    try:
        N = int(input())

        if N < 3 or N >5000:
            raise ValueError("3이상 5000이하 숫자를 입력하세요.")
        
        break   # 루프문 탈출
        
    except ValueError as error:
        print(error)


print("------------")
# <최소 봉지수 세기>
num_3 = 0
num_5 = 0

num_5 = N // 5  # 5킬로그램 봉지의 최대 개수부터 시작

while num_5 >= 0:
    나머지 = N - (num_5 * 5)  # 5킬로그램 봉지로 뺀 나머지
    if 나머지 % 3 == 0:  # 남은 무게가 3으로 나눠떨어지면
        num_3 = 나머지 // 3  # 3킬로그램 봉지 개수 계산
        print(num_5 + num_3)  # 총 봉지 개수 출력
        break
    num_5 -= 1  # 5킬로그램 봉지를 하나 줄이기
else:
    print("-1")  # 정확히 나눌 수 없는 경우
