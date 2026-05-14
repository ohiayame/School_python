"""
[문제]
 - 숫자 n을 입력받아 N부터 1까지 한 줄에 하나씩 거꾸로 출력하시오.
 - range의 step 인자에 -1을 사용합니다. (range(n, 0, -1)을 사용하세요.)
"""

n = int(input())
# range의 step 인자에 -1을 사용해 반복하여 결과 값을 출력
for i in range(n, 0, -1):
    print(i)