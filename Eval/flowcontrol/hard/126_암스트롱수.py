# 100~999 사이의 암스트롱 수를 모두 찾아 출력하세요.
# 알고리즘: 각 자리수를 분리한 뒤 세제곱 합이 원래 수와 같은지 확인

print("3자리 암스트롱 수:")
for n in range(100, 1000):
    hundreds = n // 100          # 백의 자리
    tens = (n // 10) % 10        # 십의 자리  # 변수명을 자리수 명칭으로 변경
    ones = n % 10                # 일의 자리

    if n == hundreds**3 + tens**3 + ones**3:
        print(f"{n} = {hundreds}^3 + {tens}^3 + {ones}^3")