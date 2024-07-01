# if문은 조건을 선택되는 개수가 1개밖에 없다
# elif になったってことはifの条件は絶対に違うってこと
# 위의 조건이 안 맞았으니까 여기까지 내려왔다みたいな

value = int(input("성적 입력: "))
score = ""
if value >= 90: # 90 <= value 
    score = "A"
elif value >= 80: # value >= 80만 조건이 아니고 위의 조건이 안 맞았으니까 여기까지 내려왔다 ->80 <= value < 90
    score = "B"
elif value >= 70: # 70 <= value < 80
    score = "C"
elif value >= 60: # 60 <= value < 70
    score = "D"
else:             # value < 60
    score = "F"
    
print(score)

# 주위: 조건은 중복되지 않는다, 놓친 조건이 없는지 확인

if value > 10:
    print("a")
elif value < 10:
    print("b")
    
# 이럴때는 10이 포함되지 않아서 잘 못된 조건이다