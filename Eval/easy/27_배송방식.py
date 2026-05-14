# 무게 판정 → 옵션 입력 → 최종 배송 방식 출력.
weight = float(input())
option = input()

# 무게 2kg 이상:
if weight >= 2.0:
    # 빠른 배송 Y: 택배(빠른 배송) - 5000원
    if option == "Y":
        print("택배(빠른 배송) - 5000원")
    # 일반 N: 택배(일반 배송) - 3000원
    else:
        print("택배(일반 배송) - 3000원")
# 무게 2kg 미만:
else:
    # 등기 Y: 우편(등기) - 2000원
    if option == "Y":
        print("우편(등기) - 2000원")
    # 일반 N: 우편(일반) - 1000원
    else:
        print("우편(일반) - 1000원")