# While문을 사용하여 1~1000까지의 자연수 중 3의 배수의 합
value = 0
sum = 0
while value <= 1000:
    value += 1
    if value % 3 == 0:
        sum += value
    
print("1~1000 사이 정수 중 3의 배수의 총 합은 :", sum)