# 정수를 입력 받아서 0면 "0"를 출력 0초과면 "양의 정수"를 출력
# 0미만면 "음의 정수"를 출력
value = int(input("입력"))

if value == 0:
    print("0")
elif value > 0 :
    print("양의 정수")
else:
    print("음의 정수")

# print가 많으면 안된다 

# 매번 출력 하지 않고 변수로 출력하는 이유
# -> 출력 문장이나 계산 방법을 변경할 때 효율적으로 변경이 가능
msg = ""    
if value == 0:
    msg += "0"
elif value > 0 :
    msg += "양의 정수"
else:
    msg += "음의 정수"
    
print("결과:", msg)