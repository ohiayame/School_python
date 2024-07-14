import csv
file_path = "2024_std_num_hight_school.csv"

man = [0, 0, 0]
woman = [0, 0, 0]

with open(file_path, "r", encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        try:
            man[0] += int(row['1학년(남)'])
            man[1] += int(row['2학년(남)'])
            man[2] += int(row['3학년(남)'])
            
            woman[0] += int(row['1학년(여)'])
            woman[1] += int(row['2학년(여)'])
            woman[2] += int(row['3학년(여)'])
        except:
            continue

# 전체 고등학생 수
students = 0
for i in range(3):
    students += man[i] + woman[i]
print("전체 고등학생 수:", students)

# 학년별
for i in range(3):
    print(f"{i+1}학년 - 남학생 수: {man[i]:,}, 여학생 수: {woman[i]:,}, 남학생 비율: {(man[i]/(man[i] + woman[i]) * 100):.2f}%, 여학생 비율: {(woman[i]/(man[i] + woman[i]) * 100):.2f}%")
