# 평균은 컴프리헨션 바깥에서 미리 계산해 두고, 컴프리헨션 안에서는 `x - mean` 만 표현하세요.
# 정수 나눗셈 `//` 을 사용해야 결과가 정수가 됩니다.
data = [10, 20, 30, 40, 50]
n = int(input())  # 변수명을 문제 설명의 N과 일치시킴

slice_data = data[:n]

# 평균 계산
avg = sum(slice_data) // len(slice_data)
# 컴프리헨션 안에서는 `x - mean` 만 표현
centered = [x - avg for x in slice_data]  # 변수명을 centering 결과임을 명확히 표현

# 결과 값 공백 구분하여 출력
print(*centered)