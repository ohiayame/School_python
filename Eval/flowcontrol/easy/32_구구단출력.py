# for + range(1, 10)을 사용해 구구단 한 단을 출력하세요.
dan = int(input())

# 1~9까지 반복해서 결과 값을 출력
for num in range(1, 10):
    # N x i = 값
    print(f"{dan} x {num} = {dan * num}")