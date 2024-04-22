# “1 ~ 100”까지 양의 정수 중 “3”이 포함된 정수만 출력
# for 1~100의 숫자를 반복
for num in range(1, 100):
    # for 나온 숫자를 문자형으로 바꿔서 한문자 씩 반복해서 검사
    for value in str(num):
        # if 3이 포함되면 숫자를 출력
        if value == "3":
            print(num)