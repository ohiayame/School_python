# 빈 리스트에서 시작해 N번 입력을 받아 append로 추가하세요. 출력 시 join을 활용하면 깔끔합니다.
n = int(input())

student_names = []

# n번 반복하여 이름을 입력받아 배열에 저장
for _ in range(n):
    name = input()
    student_names.append(name)

# 결과 값 출력
print(f"출석 {n}명")
print("명단:", " ".join(student_names))