# for + if + 누적 변수를 사용하세요.
total = 0
best = 0
# 5명 정의
people = 5
# 5번 반복
for _ in range(people):
    # 점수 입력 받기
    score = int(input())
    # total에 점수 추가
    total += score
    # 만약에 best보다 score가 크면 대입
    if score > best:
        best = score 

# average 계산
average = total / people

# 결과 값 출력
print(f"평균: {average:.1f}")
print(f"최고점: {best}")