# def seed_calculation(idx, seed, values):
#     # 계산에 필요한 값을 받고 2개로 분리
#     num1, num2 = values
#     # n 계산
#     n = (seed * num1 + num2) % 45 + 1
#     # 0번째 아니고 result에 포한 되어있지 않으면 n = n % 45 + 1
#     if idx != 0 and n in result:
#         n = n % 45 + 1
#     # result에 추가 하고 반환
#     result.append(n)
#     return n

# # 각 단계에서 계산에 필요한 수
# values = [(7, 3), (13, 11), (17, 7), (23, 5), (29, 13), (31, 17)]
# result = []  # 계산한 값을 저장
# # 입력 받기
# seed = int(input())

# # 6번 반복
# for idx in range(6):
#     # 0번째면 "=== 로또 번호 ===" 출력 후 입력 값을 기준이로 계산
#     if idx == 0:
#         print("=== 로또 번호 ===")
#         new_seed = seed_calculation(idx, seed, values[idx])
#     # 아니면 result[idx-1]기반으로 계산
#     else:
#         new_seed = seed_calculation(idx, result[idx-1], values[idx])
#     # 계산 결과 출력
#     print(f"번호 {idx+ 1}: {new_seed}")
# # 행운을 빕니다! 출력
# print("행운을 빕니다!")

# 위 규칙을 그대로 구현
seed = int(input())

# 각 번호 계산
n1 = (seed * 7 + 3) % 45 + 1

n2 = (n1 * 13 + 11) % 45 + 1
# 중복이면 최대 1번 보정
if n2 == n1:
    n2 = n2 % 45 + 1

n3 = (n2 * 17 + 7) % 45 + 1
if n3 in (n1, n2):
    n3 = n3 % 45 + 1

n4 = (n3 * 23 + 5) % 45 + 1
if n4 in (n1, n2, n3):
    n4 = n4 % 45 + 1

n5 = (n4 * 29 + 13) % 45 + 1
if n5 in (n1, n2, n3, n4):
    n5 = n5 % 45 + 1

n6 = (n5 * 31 + 17) % 45 + 1
if n6 in (n1, n2, n3, n4, n5):
    n6 = n6 % 45 + 1

# 출력
print("=== 로또 번호 ===")
print(f"번호 1: {n1}")
print(f"번호 2: {n2}")
print(f"번호 3: {n3}")
print(f"번호 4: {n4}")
print(f"번호 5: {n5}")
print(f"번호 6: {n6}")
print("행운을 빕니다!")