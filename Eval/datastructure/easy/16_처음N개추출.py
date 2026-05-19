# 슬라이싱 `lst[:N]` 으로 처음 N개를 한 번에 추출할 수 있습니다.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
n = int(input())

# N번째 까지의 원소 출력
print(" ".join(map(str, scores[:n])))