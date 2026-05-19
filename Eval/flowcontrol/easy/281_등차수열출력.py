# 끝값은 포함되지 않는 점에 유의해 for 반복문을 작성하세요.
start = int(input())
stop = int(input())
step = int(input())

# 1. start부터 stop 미만까지 step 간격으로 수열 생성
# 2. 각 숫자를 문자열로 변환 후 공백으로 연결하여 출력
print(' '.join(str(num) for num in range(start, stop, step)))