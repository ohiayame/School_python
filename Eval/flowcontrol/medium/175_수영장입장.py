# 나이로 기본 요금을 정하고, 오후면 50% 추가
age = int(input())
time_slot = input()

# 7세 이하: 무료
if age <= 7:
    price = 0
# 8~13세 (어린이): 3000원
elif age <= 13:
    price = 3000
# 14~18세 (청소년): 5000원
elif age <= 18:
    price = 5000
# 19세 이상 (성인): 8000원
else:
    price = 8000

# 시간대 할증: 
# 오후: 기본 요금의 50% 추가 (무료 대상은 그대로 무료)
if time_slot == "오후" and price > 0:
    price = price + price // 2  # 정수 연산으로 부동소수점 오차 방지

# 결과 값 출력
print(f"나이: {age}세 | 시간대: {time_slot}")
print(f"입장료: {price}원")