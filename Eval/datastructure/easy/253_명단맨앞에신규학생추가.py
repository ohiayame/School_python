# 기존 N명을 받아 리스트에 append 한 뒤, 마지막에 입력된 새 학생을 insert(0, ...) 로 넣으세요.
n = int(input())
names = []
# n명 이름 입력 받고 append 
for _ in range(n):
    name = input()
    names.append(name)

# 새 학생을 insert(0, ...) 로 추가
new_name = input()
names.insert(0, new_name)

print(" ".join(names))