from collections import Counter

def create_wordbook(n, m, words):
    # 길이가 M 이상인 단어만 필터링
    filtered_words = [word for word in words if len(word) >= m]

    #단어의 빈도수 계산
    word_count = Counter(filtered_words)

    # 정렬 (빈도 내림차순 > 길이 내림차순 > 사전순)
    sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

    
    return sorted_words


n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]
result = create_wordbook(n, m, words)
print("\n".join(result))
