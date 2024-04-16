import random

def value():
    random_number = random.randint(1,100)
    if num(random_number) == True:
        li.append(random_number)
    else :
        return value() 
    
def num(random_number):
    for test in li:
        if test == random_number:
            return False
    
    return True   
           
                 
while True:
    input_value = int(input("N값을 입력하세요(1-100):"))
    li = []
    if 0 < input_value <= 100 :
        for _ in range(0, input_value):
            value()
            
        print("생성된 리스트:", li)             
         
        while True:
            index = input_value - 1   
            input_num = int(input("원하는 원소의 인덱스를 입력하세요(0-{}):".format(index)))     
            if 0 <= input_num and input_num < input_value :  
                print('선택한 인덱스의 원소:', li[input_num])
                break
            
            else :
                print("에러: 유효한 인덱스 범위를 벗어났습니다.")     
                
        break    
    else:
        print("에러: N은 1이상 100이하의 정수여야 합니다.")   
        




   