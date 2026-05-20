# 정답 37을 맞추는 숫자 야구 게임
ANSWER = 37  # 상수는 대문자로 표기 (Python 컨벤션)
tens_digit = ANSWER // 10   # result1 → 자릿수 의미를 담은 이름으로 변경
units_digit = ANSWER % 10

count = 0

while True:
    # 값 초기화
    strike = 0
    ball = 0
    count += 1

    num = int(input())

    # 맞추면 종료
    if num == ANSWER:
        print(f"정답! {count}번 만에 맞춤")
        break
    else:
        # 스트라이크: 같은 자리에 같은 숫자 (각 자리를 독립 if로 처리)
        if num // 10 == tens_digit:
            strike += 1
        if num % 10 == units_digit:  # elif → if 로 변경: 두 자리 모두 독립 판정
            strike += 1
        # 볼: 다른 자리에 같은 숫자
        if num // 10 == units_digit:
            ball += 1
        if num % 10 == tens_digit:
            ball += 1

        # 결과에 따라 출력
        if strike == 0 and ball == 0:
            print("아웃")
        else:
            print(f"{strike}스트라이크 {ball}볼")