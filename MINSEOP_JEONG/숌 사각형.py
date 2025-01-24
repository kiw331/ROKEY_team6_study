def solve():
    import sys
    input = sys.stdin.readline

    N, D = map(int, input().split())

    # 정답을 담을 N x N 격자(-1로 초기화)
    grid = [[-1] * N for _ in range(N)]
    # 각 열에서 아직 등장하지 않은 숫자들을 추적하는 집합
    col_missing = [set(range(D)) for _ in range(N)]

    # row번째 행을 채우고 있을 때, col번째 열까지 채우는 중
    # used_set는 현재 행(row)에서 이미 등장한 숫자들의 집합
    def backtrack(row, col, used_set):
        # 모든 행을 다 채웠으면 (row == N)
        if row == N:
            # 이제 각 열도 모두 0..D-1을 포함했는지(col_missing이 비었는지) 확인
            for s in col_missing:
                if s:  # 아직 비어있지 않다면 실패
                    return
            # 여기까지 왔으면 조건 만족 -> 출력 후 종료
            for r in range(N):
                print(' '.join(map(str, grid[r])))
            sys.exit(0)  # (문제 환경에 따라 return으로 바꿔도 됨)
        
        # 한 행을 다 채운 경우(col == N)
        if col == N:
            # 이 행에 0..D-1이 모두 등장했는지 확인
            if len(used_set) == D:
                # 다음 행으로 넘어가며, used_set 초기화
                backtrack(row + 1, 0, set())
            return  # 다음 숫자 시도 없이 종료
        
        # (가지치기) 현재 행에서 아직 등장 안 한 숫자의 개수를
        # 남은 칸(N - col)으로 커버할 수 있는지 확인
        if D - len(used_set) > N - col:
            return  # 커버 불가능하면 되돌아감
        
        # 0..D-1을 오름차순으로 시도하여 (row, col)을 채운다
        for digit in range(D):
            # digit을 놓는다고 해서 행마다 digit을 여러 번 놓는 건 가능
            # (단, 최소 한 번은 놓여야 한다)
            # 다만 열에서 아직 digit이 등장한 적이 없으면 col_missing[col]에서 지워줘야 함
            need_in_this_col = (digit in col_missing[col])
            
            # (row, col)에 digit을 배치
            grid[row][col] = digit
            
            # 열 집합 갱신
            if need_in_this_col:
                col_missing[col].remove(digit)
            
            # 현재 행에서 새롭게 등장한 digit이면 used_set에 추가
            newly_used = (digit not in used_set)
            if newly_used:
                used_set.add(digit)
            
            # (가지치기) 각 열마다 남아있는 '필요 숫자' 개수가
            # 남은 행 개수(N - row - 1)보다 많은지 확인
            # 만약 어떤 열에서 필요한 숫자가 3개인데 남은 행이 2개뿐이면
            # 불가능하므로 가지치기
            possible = True
            rows_left = N - row - 1
            for c in range(N):
                if len(col_missing[c]) > rows_left:
                    possible = False
                    break
            
            # 만약 가능성이 있으면 다음 칸으로 진행
            if possible:
                backtrack(row, col + 1, used_set)
            
            # 되돌리기(백트래킹)
            if need_in_this_col:
                col_missing[col].add(digit)
            if newly_used:
                used_set.remove(digit)
            grid[row][col] = -1

    # 백트래킹 시작
    backtrack(0, 0, set())
