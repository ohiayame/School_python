def menu_print(menu_arr):
    print("===== 편의점 =====")
    for idx, (menu, price) in enumerate(menu_arr):
        print(f"{idx + 1}. {menu} ({price}원)")

# while True, if/elif로 메뉴 분기 후 break 처리
menu_arr = [
    ("삼각김밥", 1200),
    ("음료수", 1500),
    ("과자", 2000)
]
qty_arr = [0 for _ in range(len(menu_arr))]

while True:
    # menu출력 후 입력 받기
    menu_print(menu_arr)
    order = int(input())

    # 상품 1/2/3 외: 잘못된 상품 번호입니다. 출력 후 계속
    if not 1 <= order <= 3:
        print("잘못된 상품 번호입니다.")
        continue

    # 수량 입력 후 개수 추가
    menu_number = int(input())
    qty_arr[order - 1] += menu_number
    # 이름 N개 추가! 출력 
    print(f"{menu_arr[order - 1][0]} {menu_number}개 추가!")

    print()

    # 유효 입력 후 "계속 쇼핑?"을 입력받아 1이 아니면 break
    is_continue = int(input()) != 1
    if is_continue:
        break
    
# 계산서 출력
print("===== 계산서 =====")
total_fee = 0 # 총액

# for idx in range(len(qty_arr)):
#     # 개수 추출
#     num = qty_arr[idx]
#     # 1개 이상이면 금액 계산, 금액을 총액에 추가 후 
#     if num != 0:
#         menu, price = menu_arr[idx]
#         fee = price * num
#         total_fee += fee
#         # 이름 x 수량 = 금액원 출력
#         print(f"{menu} x {num} = {fee}원")


# zip을 사용해 인덱스 없이 두 리스트를 동시에 순회 (더 Pythonic)
for (menu, price), qty in zip(menu_arr, qty_arr):
    # 1개 이상이면 금액 계산 후 총액에 추가
    if qty > 0:
        fee = price * qty
        total_fee += fee
        # 이름 x 수량 = 금액원 출력
        print(f"{menu} x {qty} = {fee}원")

# 마지막에 총액: T원 출력
print(f"총액: {total_fee}원")