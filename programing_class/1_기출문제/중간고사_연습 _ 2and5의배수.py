# 1이상 30이하의 정수 중에 짝수이면서 5의 배수

for value in range(1,31):
    if value % 2 == 0 and value % 5 == 0:
        print(value, "\t", end = "")
        
if value % 2 == 1:
    if value % 3 == 0:
        print(value)
        
# 정수를 입력 받아 입력 받은 정수를 화면에 출력 -> 무한 반복
# 3의 배수 또는 4의 배수가 입력 되면 종료
while True:
    input_value = int(input("입력: "))

    if input_value % 3 == 0 or input_value % 4 == 0 :
        break
    print(input_value)
    
    
for count in range(1,10):
    print(count % 5 ,"\t", end = "")
    # 추력결과: 1       2       3       4       0       1       2       3       4 
    
    
# 문자열의 길이를 출력

foo = "hello"
count = 0
for char in foo :
    count += 1
print(count)