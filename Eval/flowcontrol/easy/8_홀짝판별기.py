# %(나머지) 연산자와 if/else를 사용해 홀짝을 판별하세요.
num = int(input())

# 입력 값이 2의 배수면 "짝수"를 저장 아니면 "홀수"를 저장
result = "짝수" if num % 2 == 0 else "홀수"

# 결과를 출력
print(f"{num}은(는) {result}입니다")