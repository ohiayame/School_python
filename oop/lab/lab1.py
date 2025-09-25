class Student:
    count = 0
    def __init__(self, student_id, name, eng, kor, math):
        # id count
        Student.count += 1
        # 값 초기화
        self.id = Student.count
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
        self.total = 0
        self.average = 0
    
    # 합계
    def calc_total(self):
        self.total = self.eng + self.kor + self.math
    # 평균
    def calc_average(self):
        self.average = self.total / 3
        
    # def get_eng(self):
    #     return self.eng
    # def get_kor(self):
    #     return self.kor
    # def get_math(self):
    #     return self.math
    # def set_eng(self, eng):
    #     self.eng = eng
    # def set_kor(self, kor):
    #     self.kor = kor
    # def set_math(self, math):
    #     self.math = math

# 학생 객체 생성
s1 = Student("2025001", "Kim", 90, 80, 85)
s2 = Student("2025002", "Lee", 70, 75, 80)

# 합셰 및 평균 계산
s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()

# 결과 출력
print(s1.id, s1.name, s1.total, s1.average)
print(s2.id, s2.name, s2.total, s2.average)

# 학생 객체 개수 확인
print("총 학생 수:", Student.count)