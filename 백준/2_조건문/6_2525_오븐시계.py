# 입력 (오리구이를 시작하는 시각시간
# 입력 (오븐구이를 하는 데 필요한 시간
h, m = map(int,input().split())
minute = int(input())

m < 60

if (m + minute) / 60 >= 1:
    value = (m + minute) // 60
    h += value
    m = (m + minute) - (value * 60)
    
else:
    m += minute
if h >= 24:
    h -= 24
print(h,m)