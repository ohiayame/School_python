class Student:
    # 클래스 속성
    school = "YJU"
    
    # 생성자
    def __init__(self, name, age):
        self.name = name # 인스턴스 속성
        self.age = age
    
    # 인스턴스 메서드
    def introduce(self):
        print(f"My name is {self.name}, {self.age} years old.")
    
    # 클래스 메서드
    @classmethod
    def get_school(cls):
        print("School:", cls.school)
    
    # 정적 메서드
    @staticmethod
    # def hello():
    #     print("Hello, Python OOP!")
    def add(a, b):
        print("합: ", a + b)
    
# 객체 생성 
s1 = Student("Kim", 20)

# 인스턴스 메서드 호출 -> 인스턴스 참조 변수 사용
s1.introduce() # Student.introduce(s1)

# 클래스 메서드 호출 -> 클래스 참조 변수 사용
Student.get_school()

# 정적 메서드 호출 -> 독립 유틸리티 함수 
# Student.hello()
Student.add(3, 5)

