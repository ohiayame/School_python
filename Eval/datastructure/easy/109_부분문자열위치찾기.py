# `text.find(target)` 은 없으면 -1을 반환하므로 안전하게 사용할 수 있습니다.
text = input()
target = input()

# text에서 target의 첫 등장 위치를 찾아 출력 (없으면 -1 반환)
# 첫 등장 위치를 한 줄로 출력 없으면 -1 을 출력
print(text.find(target))