# 중첩 반복문이 있을 경우,
# continue가 선언 된 블록(Block)의
# 반복문으로 이동
count = 0
while count < 3:
    for value in range(1,3):
        if count == 1:
            continue
        
        print("count : ", count, ", value : ", value) 
    count += 1