import sys
input = sys.stdin.readline

TC = int(input())

for t in range(TC):
    N, M = map(int, input().split())
    ans = cnt = 0
    p = False
    isNot = []
    
    # 펠린드롬 수인지 판별
    for _ in range(N):
        s = input().rstrip()
        if s != s[::-1]:
            isNot.append(s)
        else:
            p = True
    
    for _ in range (len(isNot)):
        tmp = isNot.pop()
        if tmp[::-1] in isNot:
            cnt += 2

    ans = cnt * M

    if p:
        ans += M
    
    print(f'#{t+1} {ans}')