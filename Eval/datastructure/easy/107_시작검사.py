# 문자열의 `startswith(prefix)` 메서드를 사용하세요.
text = input()
prefix = input()

# prefix로 시작하면 yes, 아니면 no를 출력
print("yes" if text.startswith(prefix) else "no")