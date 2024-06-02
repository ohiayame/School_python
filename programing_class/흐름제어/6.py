# 1부터 20까지의 정수 중 짝수의 합계 계산
count = 0
for num in range(1,21):
    if num % 2 != 0:
        continue    # 홀수 건너 뜀
    count += num
print("1부터 20까지의 짝수 합계 (홀수 건너 뜀):",count)