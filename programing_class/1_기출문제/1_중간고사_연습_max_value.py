# 정수 3개를 입력 받아서 제일 큰 값을 출력
# あやめのこーど
value = int(input("1번째 값: "))
value2 = int(input("2번째 값: "))
value3 = int(input("3번째 값: "))

if value >= value2 and value >= value3:
    print("제일 큰 값: ", value)
elif value2 >= value and value2 >= value3:
    print("제일 큰 값: ",value2)    
else:
    print("제일 큰 값: ",value3)    


    
# 1ばんいいやつ   
value = int(input("1번째 값: "))
value2 = int(input("2번째 값: "))
value3 = int(input("3번째 값: "))

max = value

if max < value2:
    max = value2
    
if max < value3:
    max = value3

print(max) 

# 1番いいやつのforバージョン
max = -1
for count in range(0,3):
    msg = str(count) + "번"
value = int(input("1번째 값: "))

if max < value:
    max = value

print(max) 