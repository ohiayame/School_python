# while문과 %10, //10을 사용하세요.
num = int(input())

# 각 자릿수의 합 저장 변수
total = 0

# while반복
while num:
    # num % 10 -> 1의 자리
    value = num % 10
    # value(1의 자리) total에 추가
    total += value
    # 1의 자리 지우기
    num //= 10

# 결과 값 출력
print(f"각 자릿수의 합: {total}")