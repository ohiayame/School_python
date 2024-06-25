# 숫자 맞추기 게임
import random
# while 문과 break 문을 사용하여 숫자를 맞추는 게임
# 정답 숫자 :  랜덤 1에서 100사이 
random_num = random.randint(1,100)
# 사용자가 숫자를 맞출 때까지 반복
while True:
    input_num = int(input("1부터 100사이의 숫자를 맞춰보세요:"))
    if random_num == input_num:
        print("정답입니다!")
        break    # 맞추면 반복을 종료
    elif input_num > random_num:
        print("더 작은 숫자입니다.")
    else:
        print("더 큰 숫자입니다")