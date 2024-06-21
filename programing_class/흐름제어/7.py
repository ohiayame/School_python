# 별 다이아몬드 출력
# 공백 + "*" (= 5개 ) + (별 -1)개
num = 5
# 1 -> 4
for value in range(1, num ):
    clear = " " * (num - value)
    value = "*" * (value * 2 - 1)
    print(f'{clear}{value}')
# 5 -> 1
for value in range(num , 0, -1):
    clear = " " * (num - value)
    value = "*" * (value * 2 - 1)
    print(f'{clear}{value}')