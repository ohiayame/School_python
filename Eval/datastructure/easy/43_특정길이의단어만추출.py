# `len(word) == n` 을 컴프리헨션의 if 절로 사용하세요.
words = ["apple", "cat", "banana", "fig", "kiwi", "lemon", "pear"]
n = int(input())

# 길이가 정확히 N인 단어만 리스트 컴프리헨션으로 추출해 공백으로 구분하여 한 줄에 출력
filtered_words = [word for word in words if len(word) == n]
print(" ".join(filtered_words))