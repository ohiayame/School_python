# `a, b = b, a` 한 줄로 임시 변수 없이 두 값을 동시에 교환합니다.
a = int(input())
b = int(input())
print(f"교환 전: a={a} b={b}")

a, b = b, a
# 교환 전 값과 교환 후 값을 다음 형식으로 출력
print(f"교환 후: a={a} b={b}")