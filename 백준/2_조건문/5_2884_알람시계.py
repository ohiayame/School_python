# 45분 일찍 알람 설정하기

h,m = map (int,input().split())

if m >= 45:
    m -= 45
else:
    m += 15
    h -= 1
if h < 0:
    h = 23
print(h,m)