# 합이 7인지, 더블인지 순서대로 확인
dice1 = int(input())
dice2 = int(input())
total = dice1 + dice2

# 먼저 주사위: A, B 출력
print(f"주사위: {dice1}, {dice2}")

# 합이 7이면: 럭키세븐!
if total == 7:
    print("럭키세븐!")
# 두 값이 같으면(더블): 더블!
elif dice1 == dice2:
    print("더블!")
# 그 외: 합: X
else:
    print(f"합: {total}")