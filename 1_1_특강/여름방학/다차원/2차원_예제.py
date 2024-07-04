# 직접 선언
matrix = [[1,2,3], [4,5,6],[7,8,9]]
matrix = [[0] * 3] * 5

# List Comprehension(1)
rows = 3
cols = 3
matrix = [[0 for _ in range(cols)]for _ in range(rows)]

# List Comprehension(2)
# 3x4 행렬 생성, 모든 값은 0
matrix = [[0]*4 for _ in range(3)]

# 3x2 Matrix 'bar' 생성
bar = [[10, 20],[30, 40], [50, 60]]

# 'bar'리스트의 세 번째 행(인덱스 2)의 두 번째 열(인데스 1)의 값을 출력
print(bar[2][1])

# 'bar'리스트의 세 번째 행(인덱스 0)의 두 번째 열(인데스 1)의 값을 100을 변경
bar[0][1] = 100

# 변경된 'bar' 리스트의 첫 번째 행의 두 번째 열의 값을 출력
print(bar[0][1])

# 데이터 순회
foo = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# 'foo' Matrix의 모든 원소를 순회
for row in foo:
    for item in row:
        print(item, end=" ")
    print()
    
