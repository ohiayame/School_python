import random

def generate_password(length):
# 대문자 소문자 숫자 포함하는 리스트 
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    digits = '0123456789'
    # 결합
    all_characters = uppercase_letters + lowercase_letters + digits
    # 초기화
    password = ""
    # 길이만큼 반복해서 랜덤으로 파스워드 생성
    for _ in range(length):
        password += random.choice(all_characters)
    
    uppercase = False
    lowercase = False
    value = False
    
    # 대문자있으면 
    for char in uppercase_letters:
        if char in password:
            uppercase = True
    # 소문자있으면        
    for char in lowercase_letters:
        if char in password:
            lowercase = True
    # 숫자있으면            
    for char in digits:
        if char in password:
            value = True
    # 다 True -> 생성된 파스워드 반환    
    if uppercase and lowercase and value:           
        return password
    # 아니면 하번 더
    else: 
        return generate_password(length)

# 입력 받기 
length = int(input('패스워드 길이를 입력하세요:'))
# 함수호출
password = generate_password(length)
# 결과출력
print(password)