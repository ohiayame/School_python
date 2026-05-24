# `구분자.join(리스트)` 형태로 사용합니다. 구분자가 빈 문자열이면 그냥 이어붙임.
words = ["apple", "banana", "cherry", "date"]
sep = input()

# words 의 모든 원소를 입력 받은 구분자로 이어붙인 결과를 출력
print(sep.join(words))