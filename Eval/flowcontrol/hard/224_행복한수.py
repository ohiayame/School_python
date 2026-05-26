original = int(input())

# --- 자릿수 제곱합 계산 함수 ---
def digit_square_sum(n):
    return sum(int(d) ** 2 for d in str(n))

num = original

# 최대 100번 반복으로 순환 감지 (리스트 미사용)
for i in range(100):
    next_num = digit_square_sum(num)
    print(f"단계 {i + 1}: {num} → {next_num}")

    # 행복한 수: 자릿수 제곱합이 1이 되면 종료
    if next_num == 1:
        print(f"{original}은(는) 행복한 수입니다!")
        break

    num = next_num
else:
    # 100번 반복 후에도 1이 되지 않으면 행복한 수가 아님 (for-else 활용)
    print(f"{original}은(는) 행복한 수가 아닙니다.")