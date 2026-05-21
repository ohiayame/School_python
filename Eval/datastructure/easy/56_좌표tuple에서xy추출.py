# tuple도 list처럼 `point[0]`, `point[1]` 인덱스로 원소에 접근합니다.
x = int(input())
y = int(input())

# point = (x, y) 형태의 tuple을 만들고,
point = (x, y)
# 다음 두 줄을 출력
print(f"x: {point[0]}")
print(f"y: {point[1]}")