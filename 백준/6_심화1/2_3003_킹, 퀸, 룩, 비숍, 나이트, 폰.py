# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성

input_kin, input_queen, input_look, input_bishop, input_night, input_phon = map(int,input().split())

kin = 1 - input_kin
queen = 1 - input_queen
look = 2 - input_look
bishop = 2 - input_bishop
night = 2 - input_night
phon = 8 - input_phon
print(kin, queen, look, bishop, night, phon)


############

chess = [1, 1, 2, 2, 2, 8]

a = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - a[i], end = " ")