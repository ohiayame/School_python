def password_num(password):
    msg = []
    
    for char in password:
        if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122) or (48 <= ord(char) <= 57):
            pass
        else:
            return False

    has_number = False        
    for char in password:
        # 적어도 하나의 숫자가 포함
        if char.isdigit():
            has_number = True
    # 없으면 msg에 추가       
    if  has_number == False :    
        msg.append("숫자") 

    has_uppercase = False   
    for char in password: 
        # 적어도 하나의 대문자  
        if char.isupper():
            has_uppercase = True
    # 없으면 msg에 추가         
    if has_uppercase == False:
            msg.append("대문자") 

    has_len = False
    # 비밀번호의 길이가 8자 이상
    if len(password) >= 8:
        has_len = True       
    # 아니면 msg에 추가    
    else:
        msg.append("8자 이상")
        

    # 조건 Ok        
    if has_len and has_number and has_uppercase :
        return True
    
    # 안되면 msg
    else :
        return ",".join(msg)
    
while True:
    # 사용자로부터 비밀번호 입력받는다
    password = input("비밀번호를 입력 하세요: ") 
    # True   
    if password_num(password) == True:
        print("비밀번호가 안전합니다.")
        break
    elif password_num(password) ==  False:
        print("유호한 글을 입력하세요.")
    # 추가 해야하는 조건
    else:
        print("비밀번호가 안전하지 않습니다.", password_num(password),"입력하세요")    

