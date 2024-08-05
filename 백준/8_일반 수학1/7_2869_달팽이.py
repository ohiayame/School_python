# a = 하루에 올라갈 수 있는 거리
# b = 하루에 미끄러지는 거리 
# v = 나무막대 높이
a, b, v = map (int, input().split())

# 올라가야할 거리  =  v - b
# 하루에 올라갈 수 있는 거리  =  a - b
day = (v - b) // (a - b)
if (v - b) % (a - b) != 0:
    day += 1
print(day)