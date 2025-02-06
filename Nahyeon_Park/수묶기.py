# sequence_add.py
# 예외처리는 못했음

sequence = []
# <입력 받기>
N = int(input())  # 수열의 크기
for i in range(N):
    sequence.append(int(input()))   # 수열 입력


# 음수, 양수, 1, 0을 나누어 저장 // 0은 카운트 세기
negatives = []
positives = []
ones = []
zero_count = 0

for num in sequence:
    if num < 0:  # 음수
        negatives.append(num)
    elif num > 1:  # 1보다 큰 양수
        positives.append(num)
    elif num == 1:  # 1은 따로 저장
        ones.append(num)
    else:
        zero_count += 1


# 리스트 정렬
# 음수는 오름차순(작은 값에서 큰 값)
# 양수는 내림차순(큰 값에서 작은 값)
negatives.sort()  
positives.sort(reverse=True)


max_sum = 0


# 음수 리스트 (두 개씩 묶어서 곱하고 더하기)
for i in range(0, len(negatives) - 1, 2):   # 두개씩 묶을거니까 끝인덱스-1까지, 2씩 커지게
    max_sum += negatives[i] * negatives[i + 1]
if len(negatives) % 2 == 1:         # 홀수개일때
    if zero_count > 0:              # 0이 있으면    
        max_sum += 0                # 0*i 로 처리해서 0 더하기
        zero_count -= 1             # 0쓰고나면 -1
    else:
        max_sum += negatives[-1]    # 가장 끝 인덱스 -1

# 양수 리스트 (두 개씩 묶어서 곱하고 더함)
for i in range(0, len(positives) - 1, 2):   # 두개씩 묶을거니까 끝인덱스-1까지, 2씩 커지게
    max_sum += positives[i] * positives[i + 1]
if len(positives) % 2 == 1:  # 홀수 개일 경우 마지막 양수는 더하기
    max_sum += positives[-1] # 가장 끝 인덱스 -1


# 1은 더하기
max_sum += sum(ones)


# 결과 출력
print(f"최대 합: {max_sum}")
