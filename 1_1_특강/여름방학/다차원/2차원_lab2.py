# 행(rows)과열(cols)의 수를 입력 받는다
row = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# 원소가 1씩 증가하는 리스트 생성
# li = [[( i * cols + j) + 1 for j in range(cols) ]for i in range(row)]
li = [[0 for _ in range(cols) ] for _ in range(row)]
# 출력
for r in range(row):
    for c in range(cols):
        li[r][c] = (int(input(f"Enter value for [{r}][{c}]: ")))
for i in li:
    print(*i)