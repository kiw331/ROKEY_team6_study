import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
word_dict = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    if len(word) < m:
        continue
    else:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#딕셔너리의 items함수로 각 key와 value를 튜플로 묶음. 


for i in word_dict:
    print(i[0])