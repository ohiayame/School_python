# 도형 종류에 따라 필요한 값을 입력받으세요.
# 항상 (원, 삼각형, 사각형) 중 하나 입력
shape = input()

# 원 : 넓이 = 반지름 * 반지름 * 3.14
if shape == "원":
    radius = int(input())
    result = radius * radius * 3.14
    print(f"넓이: {result:.2f}")
    
# 삼각형: 넓이 = 둘째 줄에 밑변 * 셋째 줄에 높이 / 2
elif shape == "삼각형":
    width = int(input())
    height = int(input())
    result = width * height /2
    print(f"넓이: {result:.1f}")
    
# 사각형: 넓이 = 둘째 줄에 가로 * 셋째 줄에 세로
elif shape == "사각형":
    width = int(input())
    height = int(input())
    result = width * height
    print(f"넓이: {result}")