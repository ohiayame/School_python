# For 문을 사용하여 아래 학생들의 성적에 대한 총합, 평균, 학생 수를 출력
score = [99, 29, 30, 40, 20, 60]

student_num = 0
sum = 0

for value in score:
    student_num += 1
    sum += value
    
avg = sum / student_num
print("학생 수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)
# print(f"학생 수 : {student_num}, 총점 : {sum}, 평균 : {avg}")