# 음수 인덱스도 슬라이스의 양 끝에 사용 가능합니다 — 끝에서부터의 위치를 의미합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
start_idx = int(input())
end_idx = int(input())

# data[a:b] 결과를 공백으로 구분하여 한 줄에 출력
print(*data[start_idx:end_idx])