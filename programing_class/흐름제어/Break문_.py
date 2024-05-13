# for
for value in range(10):
    print(value)
    
    # value 값이 5일 경우
    if value == 5:
        break   #Loop문 단출
print("End")

# while
while True:
    value = int(input("숫자를 입력하세요"))
    print("입력 값 : ", value)
    
    if value < 0:
        break
print("End")