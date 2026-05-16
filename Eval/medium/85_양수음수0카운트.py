# for + if/elif/else + 카운팅 변수를 사용하세요.
positive = 0
negative = 0
zero = 0

INPUT_COUNT = 10

# 10번 반복
for _ in range(INPUT_COUNT):
    # 입력 받기
    num = int(input())

    # 양수이면 positive 더하기 1
    if num > 0:
        positive += 1
    # 음수이면 negative 더하기 1
    elif num < 0:
        negative += 1
    # 0이면 zero 더하기 1
    else:
        zero += 1

# 개수 결과 값 출력
print(f"양수: {positive}개")
print(f"음수: {negative}개")
print(f"0: {zero}개")