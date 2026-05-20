# 10진법 정수를 8진법으로 변환하여 출력하세요. (oct() 사용 금지)
n = int(input())

octal_result = ""  # 변수명을 더 명확하게 수정

# 0 입력 엣지케이스 처리
if n == 0:
    print(0)
else:
    # 10진법 정수를 입력받아 8진법으로 변환
    # 8로 나눈 나머지를 앞에 붙여 역순으로 조립
    while n > 0:
        octal_result = str(n % 8) + octal_result
        n = n // 8

    print(octal_result)