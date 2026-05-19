# `lst[a:b]` 은 인덱스 a부터 b-1까지의 원소를 새 리스트로 반환합니다.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
start = int(input())
stop = int(input())

# scores[a:b] 결과를 공백으로 구분한 한 줄로 출력
print(" ".join(map(str, scores[start:stop])))