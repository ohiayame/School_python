# For문을 사용하여 다섯 개의 정수를 키보드로부터 입력 받아, 합계와 평균을 출력하는 프로그램 작성

# 변수 선언
value = 0

# for 5번 반복
for num in range(1,6):
    # 사용자로부터 값 입력 받기 
    input_num = int(input(f"{num}번째 값 입력"))   
    # 변수에 입력받은 정수를 더하기
    value += input_num
    
# 합계 : 
print("합계 :", value)
# 평균: (함계 / 5
print("평균 :", value/5)


# 양의 정수 5개를 입력 받으며 합과 평균을 출력하는  프로그램을 작성하시오
all_value = 0
for _ in range(0,5):
    value = int(input())
    all_value += value
    
print(all_value, all_value/5)

# 1番　やさしい
input_value_1 = int(input("1번째 값: "))
input_value_2 = int(input("2번째 값: "))
input_value_3 = int(input("3번째 값: "))
input_value_4 = int(input("4번째 값: "))
input_value_5 = int(input("5번째 값: ")) 

sum = input_value_1 + input_value_2 + input_value_3 + input_value_4 + input_value_5
avg = sum / 5

print("sum: ", sum, "\tavg: ", avg) 

# 2番目
input_num = 5
input_list = []
for trial_count in range(0,input_num):
    msg = str(trial_count) + "번째 입력:"
    input_value = int(input(msg))
    
    sum = sum + input_value
    
avg = sum / input_num
print(sum, avg) 


# 양수 아니면 에러 메시지
input_num = 5
input_list = []
for trial_count in range(0,input_num):
    while True:
        msg = str(trial_count) + "번째 입력:"
        input_value = int(input(msg))
        
        if input_value <= 0:
            print("에러")
        else:
            break
    sum = sum + input_value
            
avg = sum / input_num
print(sum, avg)  