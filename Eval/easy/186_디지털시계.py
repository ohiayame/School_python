# 총 초를 입력받아 HH:MM:SS 형식으로 출력하세요.
total_seconds = int(input())

# HH 부분 계산 (1시간은 3,600초)
hours = total_seconds // 3600
# total_seconds에서 hours만큼의 초를 빼기
total_seconds -= hours * 3600

# MM 부분 계산 (1분은 60초)
minuits = total_seconds // 60
# SS 부분 계산 total_seconds에서 minuits만큼의 초를 빼기
seconds = total_seconds - minuits * 60

# 결과 출력 (2자리로 0을 채워 출력 -> :02d)
print(f"{hours:02d}:{minuits:02d}:{seconds:02d}")