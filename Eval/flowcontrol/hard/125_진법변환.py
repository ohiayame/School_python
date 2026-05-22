# 10진수를 2진수로 직접 변환하세요.
# 알고리즘 흐름:
#   1. 0 입력 → 즉시 결과 출력
#   2. 양수 → 2로 반복 나누며 나머지 수집 + 과정 출력
#   3. 나머지를 역순으로 합쳐 이진수 완성

num_origin = int(input())
num = num_origin
remainders = []  # 나머지를 리스트로 수집 (역순 조합을 위해)

# 0이면 0 → 2진수: 0만 출력
if num == 0:
    print("0 → 2진수: 0")
else:
    # 첫 줄에 변환 과정:
    print("변환 과정:")

    # 각 나눗셈 단계를 n ÷ 2 = q ... 나머지 r로 출력
    while num > 0:
        remainder = num % 2
        quotient = num // 2
        print(f"  {num} ÷ 2 = {quotient} ... 나머지 {remainder}")
        remainders.append(str(remainder))  # 나머지 저장
        num = quotient

    # 역순으로 합쳐 이진수 완성 (가장 마지막 나머지가 최상위 비트)
    binary_result = "".join(reversed(remainders))
    print(f"{num_origin} → 2진수: {binary_result}")