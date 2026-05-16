# 유효성 검사 후 이름 변환과 승패 판정을 수행하세요.
user = int(input())
computer = 2

# 사용자의 선택(1=가위, 2=바위, 3=보)
action_map = ["가위", "바위", "보"]
# user == 1: 아쉽게도 졌습니다. 😢
# user == 2: 무승부입니다! 😐
# user == 3: 축하합니다! 당신이 이겼습니다! 🎉
result_map = [
    "아쉽게도 졌습니다. 😢",
    "무승부입니다! 😐",
    "축하합니다! 당신이 이겼습니다! 🎉"
]

# 결과 출력
if 1 <= user <= 3:
    print(f"당신: {action_map[user - 1]} / 컴퓨터: {action_map[computer - 1]}")
    print(result_map[user - 1])
# user < 1 또는 user > 3이면 잘못된 입력입니다. 1, 2, 3 중에서 선택하세요. 출력
else:
    print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")