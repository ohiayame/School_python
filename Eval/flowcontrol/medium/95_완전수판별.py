# 1부터 num-1까지의 약수의 합을 구해 비교
num = int(input())
total = 0

# num제외num-1번 반복
for i in range(1, num):
    # 약수면 total에 수 추가
    # 약수 공식 n % i == 0
    if num % i == 0:
        total += i

# 결과 값 출력
print(f"{num}의 약수의 합: {total}")
# total == num면 num은(는) 완전수입니다! 출력
if total == num:
    print(f"{num}은(는) 완전수입니다!")
else:
    print(f"{num}은(는) 완전수가 아닙니다.")