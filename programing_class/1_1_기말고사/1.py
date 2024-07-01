import random
# 사용자로부터 입력 받기
while True:
    input_n = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))
    if 100 <= input_n <= 1000000:
        break
    print("Please enter a number within the specified range.")
    
# 발생 횟수 리스트
dice_li = [0,0,0,0,0,0]

# n만큼 주사위를 던지기
for i in range(input_n):
    dice_num = random.randint(1,6)
    dice_li[dice_num-1] += 1

# 최대수 찾기
max_num = 0
for num in dice_li:
    if max_num <= num:
        max_num = num

# 별 개수 계산
stars_li = [0,0,0,0,0,0]
index = 0

for n in dice_li:
    stars = (n / max_num) * 10
    stars_li[index] = (int(stars))
    index += 1


# 결과 출력
print("\nDice Roll Frequency Histogram:")
for i in range(6):
    print(f"{i + 1}: {stars_li[i] * "*"} ({dice_li[i]} times, {((dice_li[i]/input_n)*100)}%)")