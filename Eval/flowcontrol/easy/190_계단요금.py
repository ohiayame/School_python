# 층수를 입력받아 각 층의 요금과 누적 요금을 출력하세요.
n = int(input())

# 누적 요금 초기화
total_fee = 0

# 층수 N번 반복하여 결과를 출력
for num in range(1, n + 1):
    # 층 요금 계산 (K층은 K*100원)
    fee = 100 * num
    # 누적 요금 계산
    total_fee += fee
    
    # 각 층 결과 값 출력
    print(f"{num}층: {fee}원 (누적: {total_fee}원)")