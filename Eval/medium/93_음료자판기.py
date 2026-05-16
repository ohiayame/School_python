def menu_print(menu_map):
    # menu_map에서 직접 읽어 출력
    for idx, (name, price) in menu_map.items():
        print(f"{idx}. {name} ({price}원)")

# while + if/elif + break/continue를 사용하세요.
money = int(input())

menu_map = {
    1: ("물", 500),
    2: ("주스", 1000),
    3: ("커피", 1500)
}

while True:
    # 500원 미만이면 반복 종료
    if money < 500:
        break
    
    # 잔액 출력
    print(f"잔액: {money}원")
    # 메뉴 출력
    menu_print(menu_map)

    # 메뉴 입력 받기
    order = int(input())

    # 1/2/3이 아니면 잘못된 선택입니다. 출력 후 다시 반복
    if order not in menu_map:
        print("잘못된 선택입니다.")
        continue
    
    # menu_map에서 메뉴와 가격 가져오기
    menu, price = menu_map[order]

    # money - price가 남으면 잔액 부족 출력 후 종료
    if money - price < 0:
        print("잔액이 부족합니다.")
        break
    # 잔액이 있으면 선택 잔액 차감 후 선택 메뉴 출력 
    else:
        money -= price
        print(f"{menu}를 선택했습니다.")

# 반복 종료 후 남은 금액: 값원 출력.
print(f"남은 금액: {money}원")