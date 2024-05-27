n, m = map(int,input().split())
li_1 = []
li_2 = []
li_3 = []
for _ in range(n):
    num = map(int,input().split())
    for i in num:
        li_1.append(i)
        
for _ in range(n):
    num =  map(int,input().split())
    for i in num:
        li_2.append(i)
        
for i in range(n * m):
    result = int(li_1[i]) + int(li_2[i])
    li_3.append(result)

for i in range(0, len(li_3), 3):
    print(*li_3[i:i+3])

#####
A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
    
##########
#############################
n, m = map(int, input().split())

# 2次元リストの入力を一度に読み取る
li_1 = [list(map(int, input().split())) for _ in range(n)]
li_2 = [list(map(int, input().split())) for _ in range(n)]

# 行列の対応する要素を足し合わせる
li_3 = [[li_1[i][j] + li_2[i][j] for j in range(m)] for i in range(n)]

# 結果を出力
for row in li_3:
    print(*row)
    