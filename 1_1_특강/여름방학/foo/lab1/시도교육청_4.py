import csv

file_path = "2024_std_num_hight_school.csv"

education_office = {}

with open(file_path, "r", encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        office_name = row['시도교육청']
        if office_name not in education_office:
            education_office[office_name] = len(education_office)
    
    education_office = list(education_office)
    
    man = [[0,0,0] for _ in range(len(education_office))]
    woman = [[0,0,0] for _ in range(len(education_office))]
            
with open(file_path, "r", encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
        
    for row in csv_reader:
        try:
            index = education_office.index(row['시도교육청'])
            man[index][0] += int(row['1학년(남)'])
            man[index][1] += int(row['2학년(남)'])
            man[index][2] += int(row['3학년(남)'])
            
            woman[index][0] += int(row['1학년(여)'])
            woman[index][1] += int(row['2학년(여)'])
            woman[index][2] += int(row['3학년(여)'])
        except:
            continue

total_li = []
sum = 0
for i in range(len(education_office)):
    for j in range(3):
        sum += man[i][j] + woman[i][j]
    total_li.append(sum)
    sum = 0   

# chat gpt
# top5
index = list(enumerate(total_li))

sorted_index = sorted(index,key=lambda x: x[1], reverse=True)

top_index = [index for index, value in sorted_index[:5]]

top_value = [total_li[i] for i in top_index]
top_name = [education_office[i] for i in top_index]
####

print("Top 5 Education Offices by Student Numbers:")
for i in range(len(top_value)):
    print(f"{top_name[i]}: Total Students = {top_value[i]:,} 명")
print()  
for i in top_index:
    print(education_office[i])
    for j in range(3):
        print(f"{j + 1}학년 - 남학생 수: {man[i][j]}명, 여학생 수: {woman[i][j]}명")
    print()