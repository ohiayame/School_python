password = input("비밀번호를 입력 하세요: ")

def password_num(password):

    has_len = False
    if len(password) >= 8:
        has_len = True
    
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            
    if has_len and has_number and has_uppercase:
        return True
    
if password_num(password):
    print("비밀번호가 안전합니다.")
else:
    print("비밀번호가 안전하지 않습니다.")    

