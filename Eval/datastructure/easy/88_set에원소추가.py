# 빈 set은 `set()` 으로 만듭니다 (`{}` 는 빈 dict). `s.add(item)` 으로 추가.
n = int(input())
texts = set()

# 하나씩 입력받아 set에 추가
for _ in range(n):
    text = input()
    texts.add(text)

# 최종 set의 원소를 정렬 후 출력
print(*sorted(texts))