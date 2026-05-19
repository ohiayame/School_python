# 10번 반복하며 양수/음수/0 분류
pos_sum = 0
neg_sum = 0
zero_count = 0

INPUT_COUNT = 10
# 10번 반복
for _ in range(INPUT_COUNT):
    # 입력 받기
    num = int(input())

    # 양수이면 pos_sum 더하기 num
    if num > 0:
        pos_sum += num
    # 음수이면 neg_sum 더하기 num
    elif num < 0:
        neg_sum += num
    # 0이면 zero_count 더하기 1
    else:
        zero_count += 1

print("양수의 합:", pos_sum)
print("음수의 합:", neg_sum)
print("0의 개수:", zero_count)