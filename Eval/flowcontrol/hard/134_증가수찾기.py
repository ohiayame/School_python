# 10부터 N 사이의 증가수를 출력하세요.
N = int(input())

for num in range(12, N + 1):
    # 문자열로 변환 후 인접 자릿수 비교
    str_num = str(num)
    # range(len-1)로 줄여 마지막 인덱스 범위 체크 불필요
    is_increasing = all(str_num[i] < str_num[i + 1] for i in range(len(str_num) - 1))
    # 순증가하는 수면 출력
    if is_increasing:
        print(num)