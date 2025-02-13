# 입력: N, K, A_s, A_e, B_s, B_e, C_s, C_e
N, k = map(int, input().split())
As, Ae, Bs, Be, Cs, Ce = map(int, input().split())

# 초기 복용 (1일 아침)
cur_max = Ae  # 첫 복용은 [A_s, A_e] 내에서 가능하며, 최적은 늦은 시간

# 전체 3N번의 복용 구간을 순서대로 처리
for day in range(0, N):  # day = 0, 1, ..., N-1
    # 해당 날의 세 끼 식사 구간 (각 구간에 day만큼 1440분을 더함)
    intervals = [
        (As + day*1440, Ae + day*1440),
        (Bs + day*1440, Be + day*1440),
        (Cs + day*1440, Ce + day*1440)
    ]
    
    for (start, end) in intervals:
        # 다음 복용은 start 시각 이상이어야 하는데, 현재까지 보장 가능한 시간은 cur_max + K
        if start > cur_max + k:
            print("NO")
            exit(0)
        # 이번 구간 내에서 늦게 복용할 수 있는 최대 시간으로 갱신
        cur_max = min(end, cur_max + k)

print("YES")
