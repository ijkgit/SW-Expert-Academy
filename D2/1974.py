# 테스트 케이스의 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스에 대해 반복합니다.
for test_case in range(1, T+1):
    # 9x9 크기의 스도쿠 퍼즐 데이터를 입력받습니다.
    data = []
    for _ in range(9):
        row = list(map(int, input().split()))
        data.append(row)
    
    # 스도쿠 퍼즐이 유효한지 확인하는 변수를 초기화합니다.
    ans = 1
    
    # 각 셀에 대해 검사합니다.
    for i in range(9):
        for j in range(9):
            # 가로 방향 중복 확인
            for k in range(9):
                if data[i][j] == data[i][k] and j != k:
                    print(i, j, data[i][j])
                    print(i, k, data[i][k])
                    ans = 0
                    break
            
            # 세로 방향 중복 확인
            for l in range(9):
                if data[i][j] == data[l][j] and i != l:
                    print(i, j, data[i][j])
                    print(l, j, data[l][j])
                    ans = 0
                    break
            
            # 3x3 영역 중복 확인
            for m in range(i//3*3, i//3*3+3):
                for n in range(j//3*3, j//3*3+3):
                    if data[i][j] == data[m][n] and (i != m or j != n):
                        print(i, j, data[i][j])
                        print(m, n, data[m][n])
                        ans = 0
                        break
    
    # 결과 출력
    print(f'#{test_case} {ans}')