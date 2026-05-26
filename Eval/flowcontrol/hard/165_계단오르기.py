goal = 10
pos = 0
step_count = 0

# 시작 시 출력 (4줄, 마지막은 빈 줄)
print("=== 계단 오르기 ===")
print("목표:", goal, "칸")
print("1칸(1) 또는 2칸(2)을 선택하여 올라가세요!")
print()

while pos < goal:
    # 잘못된 입력(숫자 외 문자)에 대한 방어 처리
    try:
        input_pos = int(input())
    except ValueError:
        print("1 또는 2를 입력하세요.")
        continue

    # 1 또는 2가 아니면 안내 메시지 출력 후 계속
    if input_pos != 1 and input_pos != 2:
        print("1 또는 2를 입력하세요.")
        continue

    # step_count와 pos 수정
    step_count += 1
    pos += input_pos
    pos = min(pos, goal)  # goal 초과 시 goal로 맞춤 (예: 9칸에서 2 입력 시 11 → 10)

    # 진행 바 출력: [####------] pos/goal칸 (N번째 이동)
    print(f"[{'#' * pos}{'-' * (goal - pos)}] {pos}/{goal}칸 ({step_count}번째 이동)")

# 목표 도달 후: 빈 줄 하나, 축하 메시지 출력
print()
print(f"축하합니다! 총 {step_count}번 만에 계단을 올랐습니다!")