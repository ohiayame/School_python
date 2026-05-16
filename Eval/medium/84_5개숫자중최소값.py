# 첫 번째 입력을 minimum으로 두고 나머지와 비교하세요.
COUNT = 5

# 5번 반복
for idx in range(COUNT):
    # 입력 받기
    num = int(input())
    # 첫번째 입력은 min_num를 초기화
    if idx == 0:
        min_num = num
    # min_num보다 입력 값이 작으면 재정의
    elif num < min_num:
        min_num = num

# 결과 값 출력
print(f"최소값: {min_num}")