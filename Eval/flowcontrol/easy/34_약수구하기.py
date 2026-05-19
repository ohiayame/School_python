# "N의 약수: "를 end=" "로 출력한 뒤, 1부터 N까지 나머지가 0인 수를 end=" "로 출력하세요.
n = int(input())

# 출력 값의 기본 형식 출력
print(f"{n}의 약수:", end=" ")

# 입력 값 만큼 반복해서 약수를 찾아 출력
for i in range(1, n + 1):
    # 약수 공식 n % i == 0
    if n % i == 0:
        print(i, end=" ")

# 마지막에 줄바꿈
print()