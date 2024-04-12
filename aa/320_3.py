# 사용자로부터 나이를 입력받는다
age = int(input("나이를 입력하세요: "))

# You are in the'(해당 영단어)'age grope.라고 출력
msg = "You are in the'{}'age grope"

# 13세에서 19세 사이는 "Teenager"  
if 13 <= age <= 19 :
    print(msg.format('Teenager'))

# 20세에서 64세 사이는 "Adult"    
elif 20 <= age <= 64 :
    print(msg.format('Adult'))

# 65세 이상은 "Senior"
elif age >= 65 :
    print(msg.format('Senior'))

# 범위에 맞지 않는 입력값에는 "Unknown age group" 출력
else:
    print(msg.format('Unknown age group'))