# `existing.add(name)` 으로 추가하면 중복은 자동으로 무시됩니다.
existing = {"윤서", "지우", "민준"}
n = int(input())

# n개의 이름을 입력 받고 add로 추가(중복 자동 제거)
for _ in range(n):
    name = input()
    existing.add(name)

# 결과 값 출력
print(f"고유 학생 수: {len(existing)}")