# 세 과목 점수를 입력 받아 평균 점수를 계산
def calculate_average(math_score, science_score, english_score):
    average = (math_score + science_score + english_score) / 3    
    
# 평균에 따른 학점 등급을 부여
# A: 90점 이상, B: 80점 이상 90점 미만, C: 70점 이상 80점 미만, D: 60점 이상 70점 미만, F: 60점 미만  
    if average >= 90 :
        score = "A"
    elif 80 <= average < 90 :
        score = "B"
    elif 70 <= average < 80 :
        score = "C"
    elif 60 <= average < 70 :
        score = "D"              
    elif average < 60 :
        score = "F"  
    
    print("평균 점수는", average, "점이고, 학점은", score,"입니다.")

# 사용자로부터 수학, 과학, 영어의 점수를 입력받는다
input_math_score = float(input("수학 점수를 입력하세요: ")) 
input_science_score = float(input("과학 점수를 입력하세요: ")) 
input_english_score = float(input("영어 점수를 입력하세요: "))

# 각 과목의 점수와 함께 평균 점수 및 해당하는 학점 등급을 출력
average = calculate_average(input_math_score, input_science_score, input_english_score)
