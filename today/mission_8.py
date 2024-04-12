# 사용자로부터 비밀번호 입력받는다
password = input("비밀번호를 입력 하세요: ")

# 문자열 길이 확인하기
# 비밀번호의 길이가 8자 이상이어야 합니다
if len(password) >= 8:

# 문자열에서 숫자 확인하기
# 비밀번호에는 적어도 하나의 숫자가 포함되어 있어야 합니다
    if any(char.isdigit()for char in password): 
          
# 문자열에서 대문자 확인하기
# 비밀번호에는 적어도 하나의 대문자가 포함되어 있어야 합니다
        if any(char.isupper()for char in password):
            msg = ("비밀번호가 안전합니다.") 
        else :
            msg = ("비밀번호는 안전하지 않습니다.")
    else :
        msg = ("비밀번호는 안전하지 않습니다.")           
else :
    msg = ("비밀번호는 안전하지 않습니다.")
                   

# 하나라도 충족하지 않는 경우, 비밀번호는 안전하지 않다고 평가
# 모든 조건이 충족될 때는 "비밀번호가 안전합니다."

print(msg)
