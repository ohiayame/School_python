# `target in text` 로 먼저 검사하고, 있으면 `text.index(target)` 으로 위치를 구하세요.
text = input()
target = input()

# in 으로 존재 여부를 확인
if target in text:
    # index 메서드 위치를 출력
    print(text.index(target))
# 없으면 없음 을 출력
else:
    print("없음")