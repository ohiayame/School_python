# 사용자로부터 문자열 입력 받기
text = list(input("주민번호를 입력하세요: "))

# li = []
text.remove("-")
li = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# 문자열의 각 문자를 한 글자씩 가져와서 출력

# for idx, elem in enumerate(text):
#     if idx <= 5:
#         cheak_num = idx + 2
#     elif idx == 7 or idx == 8:
#         cheak_num = idx + 1
#     elif 9 <= idx <= 12:
#         cheak_num = idx - 7 
#     if idx == 6 or idx == 13:
#         pass    
#     else:
#         li.append(cheak_num) 
    
total = 0 
 
for i in range(12):
    total += int(text[i]) * li[i]        
            
last_value = (11 -(total % 11)) % 10 
 
if last_value == int(text[12]):
    print("유효한 주민번호입니다.") 
else:
    print("유효하지 않은 주민번호입니다.")           