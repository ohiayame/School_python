# dict의 `in` 검사는 **키** 존재 여부를 봅니다 (값이 아님).
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 이름을 한 줄로 입력받아 dict에 있으면 있음, 없으면 없음을 출력
print("있음" if name in scores else "없음")