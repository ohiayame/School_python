# 좌표를 `(x, y)` tuple로 만든 뒤 dict의 key로 사용해 조회하세요. 존재 여부 확인은 `in` 으로.
positions = {
    (0, 0): 'A',
    (0, 1): 'B',
    (1, 0): 'C',
    (2, 3): 'X',
    (4, 4): 'GOAL',
}
x = int(input())
y = int(input())

# 존재 여부 확인하고 있으면 값 출력 / 없으면 없음 출력
if (x, y) in positions.keys():
    print(positions[(x, y)])
else:
    print("없음")