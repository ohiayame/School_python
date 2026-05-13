# <= 연산자와 if/else를 사용하세요.
battery = int(input())

# 입력 값이 20이하이면 "충전 필요" 출력
if battery <= 20:
    print("충전 필요")

# 아니면 "배터리 충분" 출력
else:
    print("배터리 충분")