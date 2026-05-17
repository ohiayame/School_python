# 15의 배수를 먼저 검사해야 함
MAX_NUM = 50

# 1부터 50까지
for num in range(1, MAX_NUM + 1):
    # 3과 5의 공배수(15의 배수)면 FizzBuzz
    if num % 15 == 0:
        print("FizzBuzz")
    # 3의 배수면 Fizz
    elif num % 3 == 0:
        print("Fizz")
    # 5의 배수면 Buzz
    elif num % 5 == 0:
        print("Buzz")
    # 아니면 num 출력
    else:
        print(num)