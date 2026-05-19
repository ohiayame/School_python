# 가로와 세로를 입력받아 별(*) 사각형을 출력하세요.
width = int(input())
height = int(input())

# 세로의 수 만큼 출력을 반복
for _ in range(height):
    # ("*" * 가로)로 가로 개수 만큼 "*"를 출력
    print("*" * width)