value_li = []
for i in ["첫", "두", "세"]:
    value = int(input(f"{i}번째 수 입력: "))
    value_li.append(value)
    

value1, value2, value3 = value_li

# 모든 수가 다른경우
if value1 != value2 and value2 != value3 and value1 != value3:
    print("모든 수가 다릅니다. 가장 큰 숫자는", max(value_li), "입니다.")
# 두 수가 같은 경우
elif value1 == value2 == value3:
    print("모든 수가 같습니다.")
# 모든 수가 같은 경우 
else:
    if value1 == value2:
        print(f"두 수가 같습니다.({value1}와 {value2})")
    elif value1 == value3:
        print(f"두 수가 같습니다.({value1}와 {value3})")
    else:
        print(f"두 수가 같습니다.({value2}와 {value3})")