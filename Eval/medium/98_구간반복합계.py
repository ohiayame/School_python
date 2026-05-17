# 모드에 따라 변환 공식을 선택하고 최고/최저 갱신
mode = int(input())
n = int(input())
max_temp = -9999
min_temp = 9999

# n번 반복
for _ in range(n):
    # 온도 입력 받기
    input_temp = float(input())
    # 공식에 따라 변환하여 출력
    if mode == 1:
        result = input_temp * 9 / 5 + 32
        print(f"변환 결과: {result:.1f}°F")
    elif mode == 2:
        result = (input_temp - 32) * 5 / 9
        print(f"변환 결과: {result:.1f}°C")
    
    # 최고/ 최저 검증
    if result > max_temp:
        max_temp = result
    if result < min_temp:
        min_temp = result

# 최고/ 최저온도 출력
print("최고 변환 온도:", max_temp)
print("최저 변환 온도:", min_temp)
