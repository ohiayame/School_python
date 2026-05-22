# `d.get(key, 기본값)` 은 키가 없을 때 KeyError 대신 기본값을 반환합니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# dict.get(key, default) 를 사용하면 한 줄로 출력
print(scores.get(name, 0))