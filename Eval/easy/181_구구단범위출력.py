# 시작단과 끝단을 입력받아 해당 범위의 구구단을 출력하세요.
start = int(input())
end = int(input())

# start ~ end단 반복
for dan in range(start, end + 1):
    # 각단은 "--- N단 ---"으로 시작
    print(f"--- {dan}단 ---")
    # 1~9 반복
    for i in range(1, 10):
        # 계산 결과 출력
        print(f"{dan} x {i} = {dan * i}")