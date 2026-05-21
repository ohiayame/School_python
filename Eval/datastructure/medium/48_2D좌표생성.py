# 행 우선이므로 바깥 for 가 행(r), 안쪽 for 가 열(c) 입니다.
r = int(input())
c = int(input())

# 이중 for 형태: [표현식 for x in 바깥 for y in 안쪽]
# (R,C) 형식으로 공백 구분하여 한 줄에 출력
print(" ".join(f"({row},{col})" for row in range(r) for col in range(c))) 