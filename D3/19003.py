# 테스트 케이스의 개수 입력
TC = int(input())

# 각 테스트 케이스에 대해 반복
for t in range(TC):
    # 현재 테스트 케이스의 N과 M 값을 입력받음
    N, M = map(int, input().split())
    
    # 답, 카운트, 회문 여부를 나타내는 플래그를 초기화
    ans = cnt = 0
    p = False
    
    # 회문 여부를 판별할 문자열을 저장할 리스트
    isNot = []
    
    # 회문 여부 판별을 위한 입력 반복문
    for _ in range(N):
        s = input().rstrip()
        
        # 문자열이 회문이 아닌 경우 리스트에 추가
        if s != s[::-1]:
            isNot.append(s)
        else:
            # 회문인 경우 플래그를 True로 설정
            p = True
    
    # 회문이 아닌 문자열들 중에서 회문을 형성할 수 있는 쌍을 찾아 카운트
    for _ in range(len(isNot)):
        tmp = isNot.pop()
        if tmp[::-1] in isNot:
            cnt += 2

    # 최종 답을 계산하여 출력
    ans = cnt * M

    # 적어도 하나의 회문이 존재하는 경우 M을 더함
    if p:
        ans += M
    
    # 현재 테스트 케이스의 결과를 출력
    print(f'#{t+1} {ans}')