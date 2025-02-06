# 입력받기
n = int(input())                            # 몇 명의 회원인지 입력받음
data = [input().split() for i in range(n)]  # 공백(스페이스바 띄어쓰기)을 기준으로 자료 구분 -> 리스트 저장

# 정렬 (나이 순, 입력 순 유지)
data.sort(key=lambda x: int(x[0]))          # sort 오름차순 정리 + 나이가 같을 경우 자동으로 입력 순서 유지

# 출력
for age, name in data:
    print(age, name)