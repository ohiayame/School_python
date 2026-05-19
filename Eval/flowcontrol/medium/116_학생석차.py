# 각 학생 점수 입력 후 target 점수를 고르고 더 높은 수 세기
print("=== 5명의 점수 입력 ===")
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
target = int(input())

# 배열로 정리
std_scores = [s1, s2, s3, s4, s5]
# 내림차순으로 정렬
sorted_arr = sorted(std_scores, reverse=True)

# 결과 출력
print(f"{target}번 학생 점수: {std_scores[target - 1]}")
print(f"석차: {sorted_arr.index(std_scores[target - 1]) + 1}등")