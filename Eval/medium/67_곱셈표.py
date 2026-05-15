# 계산 함수
def print_map(start:int, num:int):
    result = ""
    for n in range(1, num+1):
        # 곱셈 계산한 문자를 result에 추가
        result += str(start * n) + "\t"
    # 계산한 값을 반환
    return result

# print(값, end="\t")로 탭 구분 출력을 만드세요.
n = int(input())

# n + 1번 순회
for row in range(n + 1):
    # 첫번째
    if row == 0:
        # X/t에 계산 함수호출하여 결과 값을 붙여서 출력
        print(f"X\t{print_map(1, n)}")
        # 구분선 출력
        print("-" * 30)
    else:
        # i번째/t에 계산 함수호출하여 결과 값을 붙여서 출력
        print(f"{row}\t{print_map(row, n)}")