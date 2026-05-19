# for + if/elif를 사용하세요.
n = int(input())

# n번 반복
for i in range(1, n + 1):
    # 입력 받기
    score = int(input())

    # 출력할 별의 개수
    star_count = 0

    # 90점 이상: ★★★★★
    if score >= 90:
        star_count = 5
    # 80점 이상: ★★★★
    elif score >= 80:
        star_count = 4
    # 70점 이상: ★★★
    elif score >= 70:
        star_count = 3
    # 60점 이상: ★★
    elif score >= 60:
        star_count = 2
    # 60점 미만: ★
    else:
        star_count = 1
    
    # i번째 학생 ★을 점수의 등급 만큼 출력
    print(f"{i}번 학생: {'★' * star_count}")