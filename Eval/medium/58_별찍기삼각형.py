# 바깥 for문으로 줄, 안쪽 for문으로 별 개수를 제어하세요.
n = int(input())

# n번 반복하여 n개 별표 출력
for counter in range(1, n + 1):
    print("*" * counter)