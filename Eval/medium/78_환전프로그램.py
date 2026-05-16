# 통화를 선택한 뒤 환율에 맞게 계산하세요.
currency = int(input())
krw = int(input())

# 달러:1350, 엔:9, 유로:1450
exchanged_map = [
    ("달러",1350),
    ("엔", 9),
    ("유로", 1450)
]

# 입력 값이 1 ~ 3인지 확인
if 1 <= currency <= 3:
    # exchanged_map에서 통화 이름과 계산에 필요한 수 가져오기
    currency_name, rate = exchanged_map[currency - 1]
    
    # 환전 금액과 수수료 계산
    converted_amount = krw / rate
    fee = int(krw * 0.015)

    # 결과 값을 출력
    print(f"환전 금액: {round(converted_amount, 2)} {currency_name}")
    print(f"수수료 (1.5%): {fee}원")
    print(f"실 지불 금액: {krw + fee}원")

# 잘못된 입력임을 출력
else:
    print("잘못된 통화 선택입니다.")