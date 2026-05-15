# for i in range(5): num = int(input()); if num % 2 != 0: print("홀수는 건너뜁니다"); continue; total += num
# 출력은 print("짝수 합계:", total) — 콤마로 공백 하나 포함
total = 0

# 5번 순회
for _ in range(5):
    # 입력 받기
    num = int(input())
    # 홀수면 "홀수는 건너뜁니다"를 출력하여 continue로 건너뛰기
    if num % 2 != 0: 
        print("홀수는 건너뜁니다")
        continue
    # 짝수는 total에 더하기
    total += num
# (짝수 합계: 값) 형식으로 합계를 출력
print("짝수 합계:", total)