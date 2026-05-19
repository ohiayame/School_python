# 130cm 이상일 때만 보호자 입력을 받고, 그 안에서 다시 150cm 기준으로 나누세요.
height = int(input())

# 키 130cm 이상:
if height >= 130:
    # 보호자 여부 입력 빋기 (Y/N)
    guardian = input()

    # 보호자 Y: 보호자와 함께 탑승 가능합니다.
    if guardian == "Y":
        print("보호자와 함께 탑승 가능합니다.")
    # 보호자 N:
    else:
        # 키 150cm 이상: 혼자 탑승 가능합니다.
        if height >= 150:
            print("혼자 탑승 가능합니다.")
        # 키 150cm 미만: 보호자가 필요합니다.
        else:
            print("보호자가 필요합니다.")
# 키 130cm 미만: 탑승할 수 없습니다.
else:
    print("탑승할 수 없습니다.")