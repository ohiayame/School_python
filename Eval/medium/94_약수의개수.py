# # 1부터 num까지 반복하며 나머지가 0이면 약수
# num = int(input())
# count = 0

# # num번 반복
# for n in range(1, num + 1):
#     # 약수면 출력하고 count+1
#     if num % n == 0:
#         print(n)
#         count += 1

# # 결과 값을 출력
# print("약수의 개수:", count)
# ==========================================================
# 1부터 num까지 반복하며 나머지가 0이면 약수
num = int(input())

# 약수 저장 배열
num_arr = []

# num번 반복
for divisor in range(1, num + 1):
    # 약수면 출력
    if num % divisor == 0:
        num_arr.append(divisor)

# 결과 값을 출력
for result_num in num_arr:
    print(result_num)
print("약수의 개수:", len(num_arr))