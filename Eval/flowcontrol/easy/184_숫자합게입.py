# N개의 숫자를 입력받아 양수 합, 음수 합, 전체 합을 출력하세요.
n = int(input())

# 양수 합, 음수 합 변수를 초기화
positive_sum = 0  # 양수의 합
negative_sum = 0  # 음수의 합

# N번 입력을 반복 하여 입력 값에 따라 계산
for _ in range(n):
    # 입력 받기
    num = int(input())
    
    # num이 양수이면 positive_sum에 추가
    if num > 0:
        positive_sum += num
    # 아니면 negative_sum에 추가
    else:
        negative_sum += num

# 전체 합 계산
total = positive_sum + negative_sum

# 계산 결과 출력
print(f"양수 합: {positive_sum}")
print(f"음수 합: {negative_sum}")
print(f"전체 합: {total}")