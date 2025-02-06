def max_square_size(n, m, matrix):
    max_size = 1  # 최소 크기는 1

    # 모든 좌표에서 탐색 시작
    for i in range(n):
        for j in range(m):
            # 최대 가능한 확장 크기
            for k in range(1, min(n - i, m - j)):
                # 네 꼭짓점 확인
                if matrix[i][j] == matrix[i][j + k] == matrix[i + k][j] == matrix[i + k][j + k]:
                    max_size = max(max_size, (k + 1) ** 2)

    return max_size


# 입력 처리
n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

# 결과 출력
print(max_square_size(n, m, matrix))
