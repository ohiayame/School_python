# 1부터 N 사이의 완전제곱수를 출력하세요.
N = int(input())

for num in range(1, N + 1):
    # 제곱 계산
    result = num ** 2
    # N 보다 크면 종료
    if result > N:
        break
    
    # 제곱 출력
    print(result)
    