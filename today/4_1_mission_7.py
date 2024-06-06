# 입력 받기
capital = int(input("초기 자본금으 입력하세요: "))  # 초기 자본금 입력
purchase_price = int(input("주식 가격을 입력하세요: ")) # 주식 구매 가격 입력
number_of_shares = int(input("구매할 주식의 수을 입력하세요: ")) # 주식 수 입력
amount_of_sales = int(input("판매할 때의 주식 가격을 입력하세요: ")) # (판매) 주식 가격 입력

# 총 구매 비용 = 주식 구매 가격 * 주식 수   : 계산
Total_Purchase_Cost = purchase_price * number_of_shares

# 남은 자본금 = 초기 자본금 - 총 구매 비용  : 계산
remaining_capital = float(capital - Total_Purchase_Cost)
print("구매 후 남은 자본금:",remaining_capital)

# 판매 예상 이익 계산: 
# 총 판매 금액  =  주식 판매 가격 * 주식 수
total_amount_of_sales = float(amount_of_sales * number_of_shares)

# 예상 이익 또는 손실을 계산
# 이익 = 총 판매 금액　- 총 구매 비용 
Profit = total_amount_of_sales - Total_Purchase_Cost
print("예상 이익:",Profit)
# 이익 -> print("예상되는 이익입니다.")
# 손실 -> print("예상되는 손실입니다.")
print("예상되는 이익입니다."if Profit >= 0 else "예상되는 손실입니다.")

# 출력
# 주식 구매 후 남은 자본금 계산
# 주식 판매 시 예상 이익 또는 손실 계산