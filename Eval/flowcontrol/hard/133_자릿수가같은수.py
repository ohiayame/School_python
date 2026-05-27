# 1부터 N 사이에서 모든 자릿수가 동일한 수를 출력하세요.
N = int(input())

for num in range(1, N + 1):
    # 루프 변수를 덮어쓰지 않도록 별도 변수에 문자열 저장
    num_str = str(num)
    # set()으로 고유 문자 수를 확인 — 1이면 모든 자릿수가 동일
    if len(set(num_str)) == 1:
        print(num_str)