import random

def value():
    # 1~10의 숫자 random_number 
    random_number = random.randint(1,100)
    # IF NUM()함수(호출)가 TRUE면 
    if num(random_number) == True:
        # 리스트에 추가
        li.append(random_number)
    # num(random_number) == False면 value()함수 호출  
    else :
        return value() 
    
def num(random_number):
    # LI를 반복
    for test in li:
        # random_number(1~10의 숫자)가 있으면 FALSE
        if test == random_number:
            return False
    #  아니면 True
    return True   

# 반복                 
while True:
    # 사용자로부터 숫자를 입력받기
    input_value = int(input("N값을 입력하세요(1-100):"))
    # 리스트를 생성
    li = []
    # 만약에 random_number가 1~10의 숫자면
    if 0 < input_value <= 100 :
        # 0부터 random_number의 수를 반복
        for _ in range(0, input_value):
            # 함수 value를 호출
            value()
            
        print("생성된 리스트:", li)             
        # 반복 
        while True:
            index = input_value - 1 
            # INDEX를 입력 받는다  
            input_num = int(input("원하는 원소의 인덱스를 입력하세요(0-{}):".format(index)))  
            # 만약에 INDEX 범위가 맞으면   
            if 0 <= input_num and input_num < input_value :  
                print('선택한 인덱스의 원소:', li[input_num])
                break
            # INDEX범위가 아니면 반복
            else :
                print("에러: 유효한 인덱스 범위를 벗어났습니다.")     
                
        break  
    # random_number가 1~10의 숫자 아니면 반복  
    else:
        print("에러: N은 1이상 100이하의 정수여야 합니다.")   