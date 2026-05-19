# 나이와 티켓 두 값을 먼저 입력받고, 중첩 if문으로 판정하세요.
age = int(input())
ticket = input()

# 18세 미만일 경우 "18세 미만은 입장할 수 없습니다." 출력
if age < 18:
    print("18세 미만은 입장할 수 없습니다.")
# 18이상이면 ticket 여부에 따른 결과 값을 출력
else:
    if ticket == "Y":
        print("입장 가능합니다.")
    else: # N일 경우
        print("티켓을 구매해주세요.")