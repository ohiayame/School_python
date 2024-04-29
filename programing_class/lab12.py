# LAB 12
# 사용자로부터 소득 금액을 입력받아 소득세를 계산

# 소득세 계산 함수
def  calculate_tax(income):
    # 1만 10%
    if income <= 10000 :
        tax = income * 0.1
        
    # 1만 초과하고 2만 이하 15%, 1천 더하기    
    elif 10000 <= income <= 20000  :
        tax = (income - 10000) * 0.15 + 1000

    # 2만 초과 20% , 2천 5백 더하기    
    elif 20000 <= income :
        tax = (income - 20000) * 0.2 + 2500
    return tax 

# 사용자로부터 소득 금액을 입력받는다
input_income = int(input("소득 금액을 입력하세요: "))

tax = float(calculate_tax(input_income))

# 결과를 출력
print("소득세는 ", str(tax) + "달러입니다.")