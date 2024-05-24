# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
all_classscore = 0
all_value = 0
for i in range(20):
    classs, value, score = input().split()
    if score == "P":
        continue
    
    if score == "A+":
        score = 4.5
    elif score == "A0":
        score = 4.0
    elif score == "B+":
        score = 3.5
    elif score == "B0":
        score = 3.0
    elif score == "C+":
        score = 2.5
    elif score == "C0":
        score = 2.0
    elif score == "D+":
        score = 1.5
    elif score == "D0":
        score = 1.0
    else :
        score = 0
        
    if score > 0:
        classscore = float(value) * score
        all_classscore += classscore
        
    all_value += float(value)
    
if all_value != 0:
    all_avg = all_classscore / all_value 
else:
    all_avg = 0
print("{:.6f}".format(all_avg))
