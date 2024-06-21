# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

li = [[score for score in scores if score >= 90 ],  # 90 이상: '우수’
    [score for score in scores if 90 > score >= 70 ],  # 70 이상 90 미만: '양호’
    [score for score in scores if 70 > score >= 50 ],  # 50 이상 70 미만: '보통’ 
    [score for score in scores if 50 > score ]] # 50 미만: '미흡
# 평균 계산
avg_li = []
for lists in li:
    avg = 0
    for i in lists:
        avg += i
    avg_li.append(avg / len(lists))

level = ["우수", "양호", "보통", "미흡"]
# index을 활용해 결과를 출력
for i in range(4):
    print(f"{level[i]}: {li[i]} 평균: {avg_li[i]}")