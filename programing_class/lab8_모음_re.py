# 입력한 문안에 한글자라도 모음이 있는지 , 문안에 알파벳이 없으면 다시입력

while True :
    inputvalue = input("입력: ").lower()
    
    result = False
    
    if not any(char >= "A" and char <= "z"  for char in inputvalue) :
        print("다시 입력해주세요")
        continue
    
    for word in inputvalue :
    
        if word == "a" or word == "i" or word == "u" or word == "e" or word == "o":
            result = True
            
    if result:
        print("모음이 있음")
        break
    else:
        print("모음은 없음")
        break


###################################################################################
#
# def버전

# def msg(value):
#     for word in value:
#         if word == "a" or word == "i" or word == "u" or word == "e" or word == "o":
#             return True
#     return False

    
# while True :   

#     inputvalue = input("입력: ").lower()
    
#     if not any(char >= "A" and char <= "z" for char in inputvalue) :
#         print("다시 입력해주세요")
#         continue
    
    
#     word = msg(inputvalue)
#     break
# print(word)    
        