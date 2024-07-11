import matplotlib.pyplot as plt
import students_2
# 성별 데이터를 리스트로 준비
genders = ['Male', 'Female']

# lab1-2에서 계산된 각 성별의 학생 수를 리스트로 저장
students = [students_2.man, students_2.woman]
# lab1-2에서 계산된 각 성별의 학생 비율을 리스트로 저장
percentages = [students_2.p_man, students_2.p_woman]

# 막대 그래프 생성을 위한 준비 
plt.figure(figsize=(14,6))  # 전체 그래프의 크기 설정 (가로 14인치, 세러 6 인치)

# 학생 수에 대한 막대 그래프 생성
plt.subplot(1, 2, 1) # 1행 2열의 첫 번째 서브플롯 위치 지정
plt.bar(genders, students, color=['blue','pink'])   # 성별에 따른 막대 그래프, 색상 지정
plt.xlabel('Gender') # x축 레이블
plt.ylabel('Number of Students')  # y축 레이블
plt.title('Number of High School Students by Gender')  # 그래프 제목
plt.grid(True)  # 그리드 표시

# 백분율에 대한 막대 그래프 생성
plt.subplot(1, 2, 2)  # 1행 2열의 두 번째 서브플롯 위치 지정
plt.bar(genders, percentages, color=['blue','pink'])   # 백분율에 따른 막대 그래프, 색상 지정
plt.xlabel('Gender') # x축 레이블
plt.ylabel('Percentage (%)')  # y축 레이블, 백분율 표시
plt.title('Percentage of High School Students by Gender')  # 그래프 제목
plt.grid(True)  # 그리드 표시

# 그래프 표시
plt.tight_layout()  # 그래프 레이어웃을 깔끔하게 정리
plt.show()  # 생성된 그래프를 화면에 표시