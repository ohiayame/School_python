# 각 자릿수를 분리하여 한글로 변환하세요.
char_map = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
num = int(input())
result = ""
remaining = num  # 원본 num 보존을 위해 별도 변수 사용

# 천의 자리 계산 (오타 수정: 차리 → 자리)
if remaining >= 1000:
    if remaining // 1000 != 1:
        result += char_map[remaining // 1000 - 1]
    result += "천"
    remaining = remaining % 1000

# 백의 자리 계산
if remaining >= 100:
    if remaining // 100 != 1:
        result += char_map[remaining // 100 - 1]
    result += "백"
    remaining = remaining % 100

# 십의 자리 계산
if remaining >= 10:
    if remaining // 10 != 1:
        result += char_map[remaining // 10 - 1]
    result += "십"
    remaining = remaining % 10

# 1~9 계산 (이 시점에서 remaining은 0~9 범위이므로 > 0 만 확인)
if remaining > 0:
    result += char_map[remaining - 1]

# 결과 값 출력
print(result)