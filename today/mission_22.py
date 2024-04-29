# 명시적 형변환
number_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
numbers = number_str.split(',')

li = []
sum = 0

msg1 = "총합이 100을 초과하지 않았습니다."
msg2 = "입력된 모든 숫자들:"
msg3 = "최종 총합:"

for i in numbers:
    sum += int(i)
    li.append(int(i))
    
    if sum > 100:
        msg1 = "총합이 100을 초과하였습니다."
        msg2 = "현재까지의 입력값들:"
        msg3 = "현재까지의 총합:"
        break

print(msg1, "\n", msg2, li, "\n", msg3, sum, sep="")