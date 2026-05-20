# 컴퓨터 패턴과 비교하여 승패를 판정하세요.
n = int(input())

# 컴퓨터 고정 패턴
computer_pattern = ["바위", "보", "가위"]
# 각 컴퓨터 선택을 이기는 플레이어 선택
winning_choice = ["보", "가위", "바위"]  # computer_pattern 과 인덱스 대응

# 전적: [승, 패, 무]
wins, losses, draws = 0, 0, 0

for idx in range(n):
    user_input = input()
    computer_choice = computer_pattern[idx % 3]

    # 무: 선택이 같을 때
    if user_input == computer_choice:
        result = "무"
        draws += 1
    # 승: 플레이어 선택이 해당 라운드 컴퓨터를 이기는 선택일 때
    elif user_input == winning_choice[idx % 3]:  # 명시적으로 winning_choice 활용
        result = "승"
        wins += 1
    else:
        result = "패"
        losses += 1

    print(f"{idx + 1}판: 플레이어({user_input}) vs 컴퓨터({computer_choice}) -> {result}")

# 최종 결과 출력
print(f"전적: {wins}승 {losses}패 {draws}무")