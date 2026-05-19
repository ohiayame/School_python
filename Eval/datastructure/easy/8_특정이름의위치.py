# `index` 메서드는 없는 값을 찾으면 오류가 발생하므로, 먼저 `in`으로 존재 여부를 확인하세요.
names = ["윤서", "지우", "민준", "서윤", "도윤", "예준"]
name = input()

# 이름이 존재하면 idx조회하고 출력 
if name in names:
    idx = names.index(name) + 1
    print(f"{idx}번째에 있습니다")
# 없으면 명단에 없습니다 출력
else:
    print("명단에 없습니다")