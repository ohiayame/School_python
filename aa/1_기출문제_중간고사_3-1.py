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