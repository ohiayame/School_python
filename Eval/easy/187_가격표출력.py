# 단가와 수량범위 N을 입력받아 1개부터 N개까지의 가격표를 출력하세요.
price = int(input())
n = int(input())

# 1~n번 반복하여 결과값을 출력
for i in range(1, n + 1):
    print(f"{i} x {price} = {price * i}")