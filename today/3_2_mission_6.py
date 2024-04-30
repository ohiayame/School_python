def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    
    hours_per_week = hours_per_week * 15     # 총 수업 = 시수/주 × 15
    absence_hours = absence_hours + (tardy_count // 3)     # 지각 처리 규칙 ->지각 3회는 결석 1시간
    
    # 결석시수가 총 수업시수의 1/4을 초과할 경우 학점  
    if absence_hours > hours_per_week / 4 :   
        return "F(학점 미부여)"
    else:
        attendance_score = 20 - (20 * absence_hours / hours_per_week)   # 20점 - (20 × 결석시간 수 / 총 수업시간 수)
        return attendance_score

# 사용자로부터 입력을 받는다    
input_hours_per_week = int(input("주당 수업 시간을 입력하세요: "))    
input_absence_hours = int(input("결석한 총 시간을 입력하세요: "))    
input_tardy_count = int(input("지각 횟수를 입력하세요: ")) 

attendance_score = calculate_attendance_score(input_hours_per_week, input_absence_hours, input_tardy_count) 

if attendance_score ==  "F(학점 미부여)":     
    print("당신의 출력 점수는 ",attendance_score,"점입니다.")    
else :
    print("당신의 출력 점수는 %.2f점입니다." % attendance_score)    