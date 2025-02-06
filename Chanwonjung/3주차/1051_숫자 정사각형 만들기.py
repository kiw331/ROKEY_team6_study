# 문제
# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 
# 이때, 정사각형은 행 또는 열에 평행해야 한다.

# 입력
#첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
#둘째 줄부터 N개의 줄에 수가 주어진다.

#출력
#첫째 줄에 정답 정사각형의 크기를 출력한다.

#입력 
n, m = map(int, input().split()) #직사각형의 행(n)과 열(m) 입력받기
square = [input().strip() for _ in range(n)] #둘째 줄부터 n개의 줄에 수를 리스트로 입력받기
 
min_square_size = 1 # 가장 작은 정사각형의 크기 1로 초기화

for i in range(n): #i(행), j(열)는 정사각형의 좌측 상단 꼭짓점 좌표
    for j in range(m):
        for size in range(1, min(n-i, m-j)): #size++ ->정사각형 한변의 길이를 늘려가면서 가능한 정사각형 탐색
            #min 함수를 통해 현재 위치에서 만들 수 있는 최대 정사각형 크기 제한 
            #정사각형 4개의 꼭짓점 값이 같은지 확인하기 
            if (square[i][j] == square[i][j+size] 
            == square[i+size][j] == square[i+size][j+size]):
                #꼭짓점 네 개 값 같으면 정사각형 생성
                min_square_size = max(min_square_size, (size+1)**2)

print(min_square_size)

