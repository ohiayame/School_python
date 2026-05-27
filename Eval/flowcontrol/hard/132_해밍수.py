# 1부터 N 사이의 해밍수를 출력하세요.
# 알고리즘: 각 수를 2, 3, 5로 반복해서 나눈 뒤 나머지가 1이면 해밍수
N = int(input())

def is_hamming(num):
    """2, 3, 5 이외의 소인수를 갖지 않으면 True 반환"""
    remaining = num  # temp → remaining: 역할이 명확한 이름으로 변경
    for divisor in [2, 3, 5]:
        while remaining % divisor == 0:
            remaining //= divisor
    return remaining == 1

for num in range(1, N + 1):
    if is_hamming(num):
        print(num)