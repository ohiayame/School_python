# `text.split()` 은 공백 기준으로 단어 리스트를 반환합니다. N-1 인덱스로 접근.
words = input().split()  # 변수명을 words로 변경해 리스트임을 명확히 표현
n = int(input())

# n이 단어 개수 이하이면 해당 단어를, 초과하면 '없음'을 출력합니다.
print(words[n - 1] if n <= len(words) else "없음")