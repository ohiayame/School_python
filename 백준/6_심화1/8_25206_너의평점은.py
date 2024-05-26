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


###########

grade_dict = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0 }
sum_credit = 0
sum_credit_by_grade = 0

for i in range(20):
    subject, credit, grade = input().split()
    # 등급이 P가 아닌 경우만 학점 * 과목 평점을 쌓고, 학점도 쌓는다.
    # 과목 평점의 경우 앞에 정의한 dict에서 등급을 넣어 값을 가져온다
    if grade != "P":
        sum_credit = sum_credit + float(credit)
        sum_credit_by_grade = sum_credit_by_grade + credit * grade_dict[grade]

print(sum_credit_by_grade/sum_credit)