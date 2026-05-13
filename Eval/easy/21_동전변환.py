# //(몫)과 %(나머지)를 사용해 큰 동전부터 차례대로 계산하세요.
amount = int(input())

# 동전 종류 배열
coin_arr = [500, 100, 50, 10]

# 각 동전 개수 저장
total_arr = [0] * len(coin_arr)

# 잔액 계산
remain = amount
# 총 동전 수
total_coin = 0

# 동전 종류 배열을 순회
for idx, money in enumerate(coin_arr):
    if remain >= money:
        coin = remain // money    # 동전 수 계산
        remain -= coin * money    # 잔액 계산
        total_coin += coin        # 총 동전 수에 추가
        total_arr[idx] = coin     # total_arr에 저장

# 결과 출력
print(f"{amount}원 → 동전 변환:")
for i in range(len(coin_arr)):
    print(f"{coin_arr[i]}원: {total_arr[i]}개")
print(f"총 동전 수: {total_coin}개")