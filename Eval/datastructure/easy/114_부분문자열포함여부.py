# `sub in text` 형태로 부분문자열 존재 여부를 확인할 수 있습니다 (위치는 모름).
text = input()
sub = input()

# 본문에 부분문자열이 포함되어 있으면 포함, 없으면 미포함 을 출력
print("포함" if sub in text else "미포함")