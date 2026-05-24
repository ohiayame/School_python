# f-string 소수점 포맷: `f"{값:.<N>f}"` — N에 자릿수를 동적으로 넣으려면 `f"{값:.{n}f}"` 형태 사용.
value = float(input())
n = int(input())

# 소수점 N자리까지 포맷팅한 결과를 출력
print(f"{value:.{n}f}")