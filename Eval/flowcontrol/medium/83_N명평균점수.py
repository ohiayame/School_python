# for + 누적 변수를 사용하세요.
n = int(input())
# n명의 점수 합
total = 0

# n번 반복
for _ in range(n):
    # 점수 입력을 받아 total에 추가
    score = int(input())

    total += score
# 평균 계산
average = total / n

# 출력 형식: 평균 점수: 값
print(f"평균 점수: {average:.1f}")