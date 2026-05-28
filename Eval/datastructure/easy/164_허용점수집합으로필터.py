# 입력을 split 후 각 토큰을 int로 변환해 set에 추가, list 순회로 `in` 검사 후 카운트.
scores = [85, 70, 92, 95, 88, 100, 65, 90, 85, 95]

# 입력 값을 저장
nums = {int(num) for num in input().split()}

# scores에 입력 값이 몇개 있는지 검증하여 출력
print(sum(1 for score in scores if score in nums))