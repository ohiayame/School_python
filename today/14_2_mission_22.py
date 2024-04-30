# 명시적 형변환
number_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
numbers = number_str.split(',')

li = []
sum = 0
over_100_flag = False # flag立てるの大切！

for i in numbers:
    num = int(i) # 형 변환
    sum += num
    li.append(num)
    
    if sum > 100:
        over_100_flag = True
        break

# フラグ回収    
if over_100_flag:    
    print("총합이 100을 초과하였습니다.")
    print("현재까지의 입력값들:",li)
    print("현재까지의 총합:", sum)  
else:    
    print("총합이 100을 초과하지 않았습니다.")
    print("입력된 모든 숫자들:",li)
    print("최종 총합:",sum)
