# 앞쪽 K개 제거(`K:`)와 뒤쪽 K개 제거(`:-K`)를 한 슬라이스에 모두 적용하세요.
# 단, K=0 인 경우 `data[0:-0]` 은 빈 슬라이스가 되므로 따로 처리하거나 다른 형태를 써야 합니다.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
trim_count = int(input())

# 0일 경우 그대로 출력
if trim_count == 0:
    print(*data)
# 아니면 앞쪽 trim_count개와 뒤쪽 trim_count개를 제외한 값 출력
else:
    print(*data[trim_count:-trim_count])