# 1~100 사이 정수 중 7의 배수이면서, 11의 배수인 수중 제일 작은 값을 출력
for num in range(1,101):
    if num % 7 == 0 and num % 11 == 0:
        print("7과 11의 최소공배수는 :", num)
        break