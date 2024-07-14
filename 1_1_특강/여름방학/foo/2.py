import csv

with open("score.csv", 'r', encoding='utf-8') as f_handler:
    
    reader = csv.reader(f_handler)
    # next()으로 현재 열을 가르키는 포인터가 이동
    header = next(reader)
    header = next(reader)

    for item in header:
        print(item,"\t", end="")
    print()
    
    # for row in reader:
    #     for item in row:
    #         print(item,"\t", end="")
    #     print()