# For 또는 while문 사용
# for 1~5 반대 순서로 
value = int(input())
for num in range(value, 0, -1):
    # 숫자 곱하기 *
    print(" " * (value - num),num * "*")
    