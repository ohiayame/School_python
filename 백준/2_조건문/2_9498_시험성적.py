# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C
# 60 ~ 69점은 D, 나머지 점수는 F

value = int(input())
score = ""
if value >= 90: 
    score = "A"
elif value >= 80: 
    score = "B"
elif value >= 70: 
    score = "C"
elif value >= 60: 
    score = "D"
else:             
    score = "F"
print(score)