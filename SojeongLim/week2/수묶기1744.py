#chatgpt
# 문제
# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.

# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다. 둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다. 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

# 출력
# 수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.
def max_sum_with_pairs(n, numbers):
    positives = []  # 양수 저장
    negatives = []  # 음수 저장
    ones = 0        # 1의 개수 저장
    total_sum = 0   # 결과 합 저장

    # Step 1: 수열을 양수, 음수, 1로 분류
    for num in numbers:
        if num > 1:
            positives.append(num)
        elif num == 1:
            ones += 1
        else:  # num <= 0
            negatives.append(num)

    # Step 2: 양수는 내림차순 정렬, 음수는 오름차순 정렬
    positives.sort(reverse=True)
    negatives.sort()

    # Step 3: 양수를 묶어서 합산
    for i in range(0, len(positives) - 1, 2):
        total_sum += positives[i] * positives[i + 1]
    # 남은 하나가 있다면 더함
    if len(positives) % 2 == 1:
        total_sum += positives[-1]

    # Step 4: 음수를 묶어서 합산
    for i in range(0, len(negatives) - 1, 2):
        total_sum += negatives[i] * negatives[i + 1]
    # 남은 하나가 있다면 더하지 않고 버림 (0이 있는 경우와 묶이기 때문)
    if len(negatives) % 2 == 1:
        total_sum += negatives[-1]

    # Step 5: 1의 개수를 모두 더함
    total_sum += ones

    return total_sum


# 입력 처리
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 결과 출력
print(max_sum_with_pairs(n, numbers))
