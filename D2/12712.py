# 테스트 케이스의 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스에 대해 반복합니다.
for test_case in range(1, T+1):
    # 행과 열의 크기를 입력받습니다.
    N, M = map(int, input().split())
    
    # 2차원 리스트를 입력받습니다.
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    # 최종 결과를 저장할 변수를 초기화합니다.
    ans = 0
    
    # 각 요소에 대해 반복하여 최대 합을 찾습니다.
    for i in range(N):
        for j in range(N):
            # 가로 방향 합 계산
            cnt_plus = lst[i][j]
            for k in range(j-M+1, j+M):
                if 0 <= k < N and k != j:
                    cnt_plus += lst[i][k]
            
            # 세로 방향 합 계산
            for l in range(i-M+1, i+M):
                if 0 <= l < N and l != i:
                    cnt_plus += lst[l][j]
            
            # 대각선 방향 합 계산 (x자 모양)
            cnt_x = lst[i][j]
            for m in range(-M+1, M):
                dx, dy = i+m, j+m
                if 0 <= dx < N and 0 <= dy < N and (dx != i and dy != j):
                    cnt_x += lst[dx][dy]
                dx, dy = i+m, j-m
                if 0 <= dx < N and 0 <= dy < N and (dx != i and dy != j):
                    cnt_x += lst[dx][dy]
            
            # 최대 합 갱신
            ans = max(ans, cnt_plus, cnt_x)
    
    # 결과 출력
    print(f'#{test_case} {ans}')