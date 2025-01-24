from collections import Counter     # 단어의 횟수를 세는 클래스

# <단어 개수, 기준이 되는 길이 입력받기>
# split을 사용해 스페이스바 기준으로 N과 M에 넣어줌
while True:
    try:
        N, M =input("영어 지문에 나오는 단어의 개수(N)와 기준이 되는 길이(M)을 입력하세요\n").split()
        N = int(N) ; M = int(M)
        if not (1 <= N <= 100000 and 1 <= M <= 10):  # 조건 검사
            raise ValueError("N은 1 이상 100000 이하, M은 1 이상 10 이하의 값이어야 합니다.")
        break  # 올바른 입력값일 경우 루프 종료
    except ValueError as error:
        print(error)


# <길이가 M이상인 단어 저장>
words = []                  # 입력받을 단어를 저장할 빈리스트
for i in range(N):          # N개의 단어 받기
    voca = input()
    if len(voca) >=  M:     # 길이가 M 이상인 단어만 저장
        words.append(voca)  
# print(words)

# <단어의 빈도수를 딕셔너리로 반환하는 클래스Counter> [{단어:빈도수},{단어:빈도수},...]
word_count = Counter(words)
# print(word_count)



# <정렬하기>
# sorted(iterable, key=None, reverse=False)
# lambda 함수 : 익명 함수, 바로 정의하고 사용하기 가능
# key = lambda x : (-word_count[x], -len(x)) 에서 x 는 word_count에서 가져올 각각의 요소를 의미
# : 뒤에는 우선순위순으로 작성하면 됨
# 1순위 : 빈도수 높은 순  -> -부호를 사용해 내림차순으로 정렬
# 2순위 : 길이가 긴 순    -> -부호를 사용해 내림차순으로 정렬
# 3순위 : 사전순으로 정렬 -> 빈도와 길이가 같은 경우 사전순으로 정렬해야됨 (오름차순으로 정렬)
my_voca = sorted(
    word_count.keys(),                              # key()값만 뽑아오기
    key = lambda x : (-word_count[x],-len(x), x)    # 빈도수, 길이, 단어자체를 비교
    )

print("------------")
for i in my_voca:
    print(i)
