# 회원일 때만 VIP 여부를 input()으로 추가로 받으세요.
is_member = input()

# 회원 인지
if is_member == "Y":
    # vip여부를 입력 받기 (Y/N)
    is_vip = input()
    # vip면 "20% 할인 적용" 출력
    if is_vip == "Y":
        print("20% 할인 적용")
    # 아니면 "10% 할인 적용" 출력
    else:
        print("10% 할인 적용")
# 비회원이면 "할인 없음" 출력
else:
    print("할인 없음")