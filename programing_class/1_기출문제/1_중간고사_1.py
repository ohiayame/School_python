# 정수를 5개를 입력 받고 합계와 평균을 출력하는 프로그램

# 리스트를 생성
li = [] 

# 정수를 5개를 반복문으로 입력 받고 리스트에 추가
for num in range(1,6):
    input_value = int(input(f"{num}번째 값을 입력하세요: "))
    li.append(input_value)
    
# 합계의 변수를 선언
sum_value = 0
# 리스트 원소를 반복해 합계를 계산
for value in li:
    sum_value += value
# 합계결과 출력
print("합계:", sum_value) 
 
# 평균을 계산
avg_value = sum_value / 5
# 평균결과 출력 
print("평균:", avg_value)