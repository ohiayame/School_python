# N개 프레임의 볼링 점수를 계산하세요. (간소화 규칙: 스트라이크 +5, 스페어 +3)
n = int(input())
total_point = 0

for num in range(1, n + 1):
    # 1투구와 2투구 입력 받기
    first, second = map(int, input().split())  # 입력은 항상 유효
    frame_sum = first + second  # 중복 계산 방지를 위해 변수로 저장

    # 스트라이크 → 15점, 스페어 → 13점, 일반 → 합산
    if first == 10:           # 스트라이크: 10 + 보너스 5
        point = 15
    elif frame_sum == 10:     # 스페어: 10 + 보너스 3
        point = 13
    else:                     # 일반 프레임
        point = frame_sum

    # 총점 계산
    total_point += point
    # 프레임 X: Y점을 출력
    print(f"프레임 {num}: {point}점")

# 마지막에 총점: Z점을 출력
print(f"총점: {total_point}점")