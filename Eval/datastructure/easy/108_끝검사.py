# 문자열의 `endswith(suffix)` 메서드를 사용하세요.
text = input()
suffix = input()

# 본문이 suffix로 끝나면 yes, 아니면 no를 출력
print("yes" if text.endswith(suffix) else "no")