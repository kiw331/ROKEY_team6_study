# 영단어 암기는 괴로워 s3
from sys import stdin
n, m = map(int, input().split())

words = {}
for _ in range(n):
    word = stdin.readline().rstrip()    #input() 쓰면 시간초과
    
    if len(word) >= m:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
            
words = list(words.items())
words.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in words:
    print(word)