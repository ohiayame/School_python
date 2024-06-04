# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

li = [[score for score in scores if score >= 90 ],  # 90 이상: 'A’
    [score for score in scores if 90 > score >= 80 ],  # 80 이상 90 미만: 'B’
    [score for score in scores if 80 > score >= 70 ],  # 70 이상 80 미만: 'C’
    [score for score in scores if 70 > score >= 60 ],  # 60 이상 70 미만: 'D’ 
    [score for score in scores if 60 > score ]] # 60 미만: 'F'
# 평균 계산
avg_li = []
for lists in li:
    avg = 0
    for i in lists:
        avg += i
    avg_li.append(avg / len(lists))

level = ["A", "B", "C", "D","F"]

# index을 활용해 결과를 출력
print("등급 분포 및 평균 점수:")
for i in range(5):
    print(f"{level[i]} 등급: 평균 점수 = {avg_li[i]:.2f}\n{"*" * len(li[i])} ({len(li[i])}명)")