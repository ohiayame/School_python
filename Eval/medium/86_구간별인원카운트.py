# for + if/elif/else + 카운팅 변수를 사용하세요.
a_count = 0
b_count = 0
c_count = 0
d_count = 0

INPUT_COUNT = 10

for _ in range(INPUT_COUNT):
    # 입력 받기
    score = int(input())

    # 점수에 따라 해당 변수에 +1
    # 90점 이상
    if score >= 90:
        a_count += 1
    # 80점 이상 90점 미만
    elif score >= 80:
        b_count += 1
    # 70점 이상 80점 미만
    elif score >= 70:
        c_count += 1
    # 70점 미만
    else:
        d_count += 1

# 결과 값 출력
print(f"90점 이상: {a_count}명")
print(f"80점 이상: {b_count}명")
print(f"70점 이상: {c_count}명")
print(f"70점 미만: {d_count}명")