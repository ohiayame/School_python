# 1!부터 N!까지 출력하고 합을 구하세요.
n = int(input())
factorial = 1      # 현재 팩토리얼 값 (누적 곱)
total_sum = 0      # 팩토리얼 합계 누적 — factorial_list + sum() 대신 변수 하나로 관리

# 1~n까지 반복
for num in range(1, n + 1):
    factorial *= num   # 조건 없이 항상 곱해도 동일 (1*1=1)
    total_sum += factorial  # 루프 안에서 바로 누적하여 리스트 불필요
    print(f"{num}! = {factorial}")

# 1! + 2! + ... + N! = 합 형식으로 총합을 출력
terms = " + ".join(f"{i}!" for i in range(1, n + 1))
print(f"{terms} = {total_sum}")