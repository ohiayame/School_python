import csv

# with open("2024_std_num_hight_school", "r", encoding="utf-8") as f_hendler:
#     reader = csv.DictReader(f_hendler)
#     li = []
#     for row in reader:
#         if row not in li:
#             li.append(row['교육지원청'])

#     for i in range(len(li)):
#         print(f"{i + 1}번, {li[i]}")

file_path = "2024_std_num_hight_school.csv"

education_office = set()

with open(file_path, "r", encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        education_office.add(row['교육지원청'])

for index, item in enumerate(education_office, start=1):
    print(f"{index}번 {item}")