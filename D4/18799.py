# 테스트 케이스의 수 T를 입력 받음
T = int(input())

# 부분집합의 평균을 계산하는 함수 정의
def avg(num):
    return sum(num) / len(num)

# 각 테스트 케이스에 대해 반복
for t in range(1, T + 1):
    # 집합의 크기 n 입력
    n = int(input())
    
    # 집합 S를 구성하는 n개의 정수를 리스트로 입력
    S = list(map(int, input().split()))
    
    # 부분집합을 저장할 리스트를 초기화하고, 전체 부분집합의 평균을 저장할 변수 tot를 초기화
    subset = [[]]
    tot = 0
    
    # 집합 S의 각 원소에 대해 부분집합을 생성하고 그 평균을 계산
    for s in S:
        size = len(subset)
        for i in range(size):
            num = subset[i] + [s]
            subset.append(num)
            tot += avg(num)
    
    # 전체 부분집합의 평균을 계산하고 소수점 아래 20자리까지 반올림하여 결과를 저장
    res = round(tot / (len(subset) - 1), 20)
    
    # 결과 출력
    print(f'#{t} {res}')