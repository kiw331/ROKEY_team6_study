# 못 풀었어요

# def can_take_medicine(n, k, meals):
#     # 복용 가능한 시간대 리스트 초기화
#     possible_times = set(range(0, 1440, k))

#     # 식사 시간대 제거
#     for start, end in meals:
#         for t in range(start, end):
#             if t in possible_times:
#                 possible_times.remove(t)

#     # 약 복용 가능 여부 확인
#     if len(possible_times) >= n:
#         return "YES"
#     else:
#         return "NO"


# # 입력 처리
# n, k = map(int, input().split())
# meals = [tuple(map(int, input().split())) for _ in range(3)]

# # 결과 출력
# print(can_take_medicine(n, k, meals))
