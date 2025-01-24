import sys
input = sys.stdin.readline

#.rstrip => 인자가 없을 경우 오른쪽 공백 제거
# input 대신 sys.stdin.readline사용했기 떄문에  문자열을 저장하기 위해 .rstrip()을 추가
N, M = map(int, input().rstrip().split())
word_list = {}

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:  # 단어 길이가 M 이상일 때만 처리
        if word in word_list:
            word_list[word] += 1  # 이미 있는 단어는 빈도 증가
        else:
            word_list[word] = 1  # 새 단어는 빈도를 1로 초기화

# 정렬 기준: 빈도 내림차순 -> 길이 내림차순 -> 알파벳 오름차순
sorted_words = sorted(word_list.keys(), key=lambda x: (-word_list[x], -len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)