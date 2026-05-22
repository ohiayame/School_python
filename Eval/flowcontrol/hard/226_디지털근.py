# while로 자릿수 합을 반복하되, 덧셈식 문자열도 함께 구성
num = int(input())
step = 0

# num >= 10 조건으로 수정: 정확히 10인 경우도 한 단계 처리
while num >= 10:
    # num를 순회하고 하나씩 분리
    digits = [int(d) for d in str(num)]
    # 단계 + 1
    step += 1
    # 합 계산 (digit_sum: 자릿수 합임을 명확히 표현)
    digit_sum = sum(digits)
    # 단계 K: 자릿수 합 계산 A → B 출력
    print(f"단계 {step}: 자릿수 합 계산 {'+'.join(map(str, digits))} → {digit_sum}")

    # num에 합을 대입
    num = digit_sum

# 마지막에 디지털 근: X 을 출력
print(f"디지털 근: {num}")