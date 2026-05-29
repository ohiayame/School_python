# `counts[w] = counts.get(w, 0) + 1` 패턴이 dict 빈도 카운트의 정석입니다.
words = input().split()
counts = {}

# counts[w] = counts.get(w, 0) + 1로 빈도 카운트
for word in words:
    counts[word] = counts.get(word, 0) + 1 

# 계산한 값 출력
for word, count in counts.items():
    print(f"{word}: {count}")