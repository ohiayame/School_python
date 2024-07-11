import csv
file_path = "2024_std_num_hight_school.csv"

man = 0
woman = 0

with open(file_path, "r", encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        try:
            man += int(row['계(남)'])
            woman += int(row['계(여)'])
        except:
            continue

students = man + woman
p_man = (man / students * 100)
p_woman = (woman / students * 100)
print(f"전체 고등학생 수: {students:,} 명")
print(f"남성 고등학생 수: {man:,} 명")
print(f"여성 고등학생 수: {woman:,} 명")
print(f"남성 고등학생 비율: {p_man:.2f} %")
print(f"여성 고등학생 비율: {p_woman:.2f} %")