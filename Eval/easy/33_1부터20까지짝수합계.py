# 1부터 20까지 반복하며 짝수(i % 2 == 0)만 합계에 누적하세요.
total = 0

min_num = 1
max_num = 20

# 1부터 20까지 반복
for i in range(min_num, max_num + 1):
    # 짝수(i % 2 == 0)면 total에 더하기
    if i % 2 == 0:
        total += i

# 결과 출력
#  1~20 짝수 합계: 110
print(f"{min_num}~{max_num} 짝수 합계: {total}")