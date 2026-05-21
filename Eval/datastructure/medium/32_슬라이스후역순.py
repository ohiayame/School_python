# 슬라이스 결과에 다시 `[::-1]` 을 체이닝하면 한 줄로 풀립니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 슬라이스 시작/끝 인덱스 입력
start_idx = int(input())  # 인덱스임을 명시하는 변수명
end_idx = int(input())

# data[a:b] 슬라이스를 역순으로 출력
print(*data[start_idx:end_idx][::-1])