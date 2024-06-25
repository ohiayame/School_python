# # 1을 10번 출력
# for _ in range(10):
#     print(1)
    
# # range(반복 횟수)
# # range(시작값, 종료값)
# # range(시작값, 종료값, 증감값)
# for num in range(10, 1):
#     print(num)
    
# 1 ~ 20 li
# # list comprehension -> 리스트 내 원소 값을 for을 사용해 동적으로 생성
# li = list ( i for i in range(1, 21))
# print(li)

# # 7를 8개 li
# li = [ 7 for _ in range(8)]
# print(li)

# # 1 ~ 20 3의 배수
# li = [value for value in range(1, 21) if value % 3 == 0 ]
# print(li)



# foo = ["abc", "dcd", "ef", "gh"]

# # 리스트중 c가 포함된 단어만 선택
# # c_li = [msg for msg in foo for char in  msg if char == "c"]
# c_li = [msg for msg in foo if "c" in msg ]
# print(c_li)

# # 리스트중 글자개수가 3개 이상
# len_li = [msg for msg in foo if len(msg) >= 3]
# print(len_li)

# # 1~10사이 정수 홀수  -> X10 짝수 -> 20
# li = [ num * 20  if num % 2 == 0  else num * 10 for num in range(1,11) ]
# print(li)

# # and 와 같은 의미
# s_list = [value for value in range(1, 21) if value % 3 == 0 if value % 4 == 0]
# print(s_list)

# # 양수가 아니면 재입력
# while True:
#     value = int(input())
#     if value > 0:
#         break
# print(value)


# while문 1~10 출력
num = 0
while num < 10:
    num += 1
    print(num)

for value in range(10):
    if value == 5:
        break
    print(value)