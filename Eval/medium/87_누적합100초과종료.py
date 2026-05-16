# while True + break를 사용하세요.
total = 0
count = 0

# 100을 넘을 때까지 반복
while True:
    # 입력 받기
    num = int(input())
    # 누적 변수에 num 더하기
    total += num
    # count 더하기 1
    count += 1

    # total이 100을 넘으면 break
    if total > 100:
        break

# 결과 값 출력
print("누적합이 100을 초과했습니다!")
print(f"누적합: {total}")
print(f"입력 횟수: {count}")