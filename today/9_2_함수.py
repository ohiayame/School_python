# def number_check(text):
#     text.replace("-", "")
#     li = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    
#     total = 0 
#     for i in range(12):
#         total += int(text[i]) * li[i]        
                
#     last_value = (11 -(total % 11)) % 10 
#     return "유효한 주민번호입니다."if last_value == int(text[12]) else "유효하지 않은 주민번호입니다."

# print(number_check(input("주민번호를 입력하세요: ")))

def get_check_value(arg_ssid):
    # li = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid_list = [int(value) for value in arg_ssid]
    
    total = sum([ssid_list[index] * weight[index] for index in range(12)])
    
    check_digit = (11 -(total % 11)) % 10 
    
    return check_digit
    

def is_valid_ssid(text):
    text = text.replace("-","")
    if len(text) != 13:
        return False
    
    check_digit = get_check_value(text[:-1])
    
    if check_digit == int(text[-1]):
        return True
    else:
        return False
result = is_valid_ssid(input("주민번호를 입력하세요: "))
print("유효한 주민번호입니다."if result else "유효하지 않은 주민번호입니다.")