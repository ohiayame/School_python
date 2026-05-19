# for + if를 사용하세요.
n = int(input())
count = 0

# N번 반복
for _ in range(n):
    # 입력 받기
    score = int(input())

    # 60점 이상이면 count +1
    if score >= 60:
        count += 1

# 결과 값 출력
print("합격자 수:", count)
