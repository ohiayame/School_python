# 자율학습 14 / mission_22
input_num_list = input("")

num_list = input_num_list.split(",")

sum = 0
output_list = []
over_100_flag = False

for num_str in num_list:
    num = int(num_str)
    sum += num
    output_list.append(num)
    
    if sum > 100:
        over_100_flag = True
        break
    
if over_100_flag:
    print("100 초과", sum)
    print(output_list)
else:
    print("100 이하", sum)
    print(output_list)