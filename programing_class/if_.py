# color = input()
# car = ""
# if color == "black" or color == "blue":
#     car = "hyundai"
# elif color == "red":
#     car = "ford"
# elif color == "grey":
#     car = "bentry"
# print (car)

####################

# color = input("자동차 모델을 입력하세요")

# if color == "M3" or color == "M5" or color == "M7":
#     car = "BMW"
# elif color == "X" or color == "Y":
#     car = "Tesla" 
# elif color == "ES" or color == "LS":
#     car = "Lexus"
# elif color == "G80" or color == "G90":
#     car = "Hyundai"
# else:
#     car = "알 수 없는 모델입니다"
# print(car)

color = input("자동차 모델을 입력하세요")

li_bmw = ["M3", "M5","M7","M8","M9"]
li_tesla = ["X", "Y"]
li_lexus = ["ES", "LS"]
li_hyundai = ["G80","G90"]
car = "알 수 없는 모델입니다"

for li, model in [(li_bmw, "BMW"), (li_tesla, "Tesla"), (li_lexus, "Lexus"), (li_hyundai, "Hyundai")]:
    for i in li:
        if i == color:
            car = model
            break
    if car != "알 수 없는 모델입니다":
        break

print(car)

# test = ["a", "b", "c", "d"]
# print("a" in test)
# print("b" in test)
# print("c" in test)
# print("d" in test)
# print("e" in test)


model = input("자동차 모델을 입력 하세요: ")

# M1, M2, M4, M6, M8, M9, M3, M5, M7    -> BMW, 
# Y, X          -> Tesla, 
# ES, LS        -> Lexus
# G80, G90      -> Hyundai
# 이외 모델      -> "알수 없는 모델입니다."
list_bmw = ["M1", "M2", "M4", "M6", "M8", "M9", "M3", "M5", "M7"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_genesis = ["G80", "G90"]

maker = ""

# bmw
for model_in_list in list_bmw:
    if model == model_in_list:
        maker = "bmw"
        break
        
# tesla
if maker == "":
    for model_in_list in list_tesla:
        if model == model_in_list:
            maker = "tesla"
            break
    
# lexus
if maker == "":
    for model_in_list in list_lexus:
        if model == model_in_list:
            maker = "lexus"
            break
    
# genesis
if maker == "":
    for model_in_list in list_genesis:
        if model == model_in_list:
            maker = "genesis"
            break

# maker = maker if maker != "" else "알수 없는 모델입니다."

# if model in list_bmw:
#     maker = "bmw"
# elif model in list_tesla:
#     maker = "tesla"
# elif model in list_lexus:
#     maker = "lexus"
# elif model in list_genesis:
#     maker = "genesis"
# else:
#     make = "Unkown model"

print(maker)
