# 언패킹은 `좌변의 변수 개수`와 `tuple 원소 개수`가 같아야 합니다.
r = int(input())
g = int(input())
b = int(input())

# color = (r, g, b) tuple을 만든 뒤,
color = (r, g, b)
# 언패킹(한 줄에 r, g, b = color)으로 세 변수를 받고 다음 형식으로 출력
r, g, b = color

print(f"R: {r}")
print(f"G: {g}")
print(f"B: {b}")