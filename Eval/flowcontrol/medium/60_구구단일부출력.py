# 바깥 for문은 단, 안쪽 for문은 곱하는 수(1~9)입니다.
# 시작 단 a와 끝 단 b를 입력받기
start_dan, end_dan= map(int, input().split())

# 바깥 for문은 단 a~b
for dan in range(start_dan, end_dan + 1):
    # 각 단의 시작에 --- N단 ---을 출력
    print(f"--- {dan}단 ---")

    # 안쪽 for문은 곱하는 수(1~9)
    for num in range(1, 10):
        # N x 1 = N 형식으로 1~9까지 출력
        print(f"{dan} x {num} = {dan * num}")
    
    # 각 단이 끝나면 빈 줄을 한 줄 출력
    print()