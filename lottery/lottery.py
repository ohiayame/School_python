from random import randint

# 1부터 45까지의 숫자 중 중복 없이 n개 뽑는 함수
# 1から45までの数字のうち、重複なくn個を選ぶ関数
def generate_numbers(n):
    li = []
    while len(li) < n:
        num = randint(1,45)
        flag = True
        for i in li:
            if i == num :
                flag = False
        if flag:
            li.append(num)
    return li

# 6개의 숫자를 뽑은 후 순서대로 정렬, 보너스 숫자 뽑는 함수
# 6個の数字を選んで順番どおり整列、ボーナス数字引き関数
def draw_winning_numbers():
    n = 7
    num = generate_numbers(n)
    # bonus = num[0]
    # num.pop(0)
    num.sort()
    return num

# 숫자와 당첨 숫자를 전달하면 맞는 갯수를 계산해주는 함수
# 数字と当選数字を伝達すれば合う個数を計算してくれる関数
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    bonus = False
    for num_1 in numbers:
        for num_2 in winning_numbers[:6]:
            if num_1 == num_2 :
                count += 1
        if num_1 == winning_numbers[-1]:
            bonus = True
    return count, bonus

# 뽑은 숫자와 당첨 숫자를 전달하면 당첨금을 계산해주는 함수
# 選んだ数字と当選数字を伝えすれば当選金を計算してくれる関数
# 6 1등         500000000
# 5 + 1 2등     5000000
# 5 3등         500000
# 4 4등         50000
# 3 5등         5000
def check(numbers, winning_numbers: list):
    count, bonus = count_matching_numbers(numbers, winning_numbers)
    
    if count == 6:    
        prize = 500000000
    elif count == 5:
        if bonus:
            prize = 5000000
        else:
            prize =  500000
    elif count == 4:
        prize = 50000
    elif count == 3:
        prize = 5000
    else:
        prize = 0
    return prize
^^;