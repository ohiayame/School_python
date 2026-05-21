# `points[n-1]` 으로 N번째 tuple을 얻고, 그 tuple을 다시 인덱스 또는 언패킹으로 분리합니다.
points = [(1, 2), (3, 4), (5, 6), (7, 8), (-1, -2)]
n = int(input())

# points[n-1]에서 x, y 추출 후 출력
x, y = points[n-1]

print(f"x: {x}")
print(f"y: {y}")