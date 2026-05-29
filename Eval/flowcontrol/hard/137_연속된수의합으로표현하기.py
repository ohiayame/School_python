# N을 연속된 자연수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input())

# 슬라이딩 윈도우: start~end 범위의 연속 자연수 합을 추적
start = 1
end = 1
window_sum = 1

while end <= N // 2 + 1:  # end가 N/2 초과 시 2개 합이 N보다 커지므로 종료
    if window_sum == N and end - start >= 1:  # 2개 이상인 경우만 출력
        numbers = list(range(start, end + 1))
        print(f"{N} = {' + '.join(map(str, numbers))}")
        # 출력 후 윈도우를 오른쪽으로 확장
        end += 1
        window_sum += end
    elif window_sum < N:
        # 합이 부족하면 오른쪽 경계 확장
        end += 1
        window_sum += end
    else:
        # 합이 초과하면 왼쪽 경계를 한 칸 축소
        window_sum -= start
        start += 1