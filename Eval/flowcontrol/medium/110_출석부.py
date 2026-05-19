# N명에 대해 이름, 상태를 반복 입력받아 분류
n = int(input())
present = 0
absent = 0

# N명에 대해 이름, 상태를 반복 입력
for _ in range(n):
    name = input()
    is_present = int(input())

    # 각 학생에 대해 
    # 이름 - 출석 또는 이름 - 결석을 출력
    if is_present:
        print(f"{name} - 출석")
        present += 1
    else:
        print(f"{name} - 결석")
        absent += 1

# 결과 값 출력
print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")