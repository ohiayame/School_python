# 문자열을 입력받아 같은 문자가 연속으로 가장 많이 반복된 횟수를 출력하세요.
s = input()

# 최대 값 저장 변수
max_count = 0
# 현재 문자와 연속 수 저장
current_char = ""
current_count = 0

# 입력 받은 txt 순회
for txt in s:
    # 만약에 이전 문자와 다르면
    if txt != current_char:
        # 새로운 문자를 등록 (초기화)
        current_char = txt
        current_count = 1
    # 동일 문자면 연속 수 더하기 1
    else:
        current_count += 1
    
    # 현재 저장되어 있는 문자의 연속 수가 크면 재정의
    max_count = max(max_count, current_count)

# 결과 값 출력
print(max_count)