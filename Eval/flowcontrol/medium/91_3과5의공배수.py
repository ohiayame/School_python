# for + if (i % 3 == 0 and i % 5 == 0)을 사용하세요.
MAX_NUM = 100

NUM_1 = 3
NUM_2 = 5

# MAX_NUM번 반복
for num in range(1, MAX_NUM + 1):
    # 3과 5 모두의 배수(= 15의 배수)면 출력
    if num % (NUM_1 * NUM_2) == 0:
        print(num)