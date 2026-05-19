# 흙 상태로 먼저 분기하고, 그 안에서 햇빛 세기를 검사하세요.
soil_dry:bool = input() == "True"
strong_sun:bool = input() == "True"

# 1. 흙이 말랐을 때
if soil_dry:
    # 1-1. 햇빛이 강하면 → 물 듬뿍
    if strong_sun:
        print("물 듬뿍")
    # 1-2. 햇빛이 강하지 않으면 → 물 조금
    else:
        print("물 조금")
# 2. 흙이 마르지 않았으면 → 물 안 줘도 돼요
else:
    print("물 안 줘도 돼요")