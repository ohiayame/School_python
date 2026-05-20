# 조건 검사 시 대소문자 차이를 없애려면 `c.lower() in "aeiou"` 가 편합니다.
# 결과를 한 문자열로 이어 붙이려면 `"".join(...)` 을 사용하세요.
s = input()

# 리스트 컴프리헨션으로 모음(a, e, i, o, u — 대소문자 모두)만 골라 그 순서대로 이어 붙인 결과를 한 줄에 출력
print("".join(char for char in s if char.lower() in "aeiou"))