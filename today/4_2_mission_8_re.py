password = input("비밀번호를 입력 하세요: ")

def password_num(password):
    flag = False
    if len(password) >= 8:
        for char in password:
            if char.isupper():
                flag = True    
    return flag

flag = password_num(password) 
print("비밀번호가 안전합니다."if flag else "비밀번호가 안전하지 않습니다.")